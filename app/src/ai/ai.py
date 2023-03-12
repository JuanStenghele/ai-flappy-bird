import neat

from typing import List
from src.constants import *
from src.obj.bird import Bird
from src.builder import Builder
from src.file_dal import FileDal
from src.output import *
from src.ai.saver import Saver

# Class that represents an Ai controlled bird
class IntelligentBird:
  def __init__(self, bird: Bird, genome, net: neat.nn.FeedForwardNetwork) -> None:
    self.bird = bird
    self.genome = genome
    self.net = net

  def jump(self, bird_y: float, next_pipe_top: float, next_pipe_bot: float) -> None:
    output = self.net.activate((bird_y, abs(bird_y - next_pipe_top), abs(bird_y - next_pipe_bot)))
    if output[0] > AI_JUMP_TRIGGER:
      self.bird.jump()

  def move(self):
    self.reward(AI_MOVE_REWARD)
    self.bird.move()

  def get_game_bird(self):
    return self.bird

  def reward(self, reward):
    self.genome.fitness += reward

  def reward_score(self):
    self.reward(AI_SCORE_REWARD)

  def punish(self, punish):
    self.genome.fitness -= punish

  def punish_collision(self):
    self.punish(AI_COLLISION_PUNISHMENT)

GENOME = 'genome'
NET = 'net'

TRAIN_MODE = 0
DISPLAY_MODE = 1

# Encapsulates the NEAT Ai
class Ai:
  def __init__(self, population: neat.Population) -> None:
    self.population = population
    self.winner = None
    self.genome_data = []
    self.birds = []
    self.mode = TRAIN_MODE
    self.fileDal = None

  # Sets display mode
  def set_display_mode(self, simulation_file: str) -> None:
    self.mode = DISPLAY_MODE
    self.fileDal = FileDal(simulation_file)

  # Add a stdout reporter to show progress in the terminal.
  def add_reporter(self):
    self.population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    self.population.add_reporter(stats)

  # Runs the game to train the birds
  def run(self, game_runner) -> None:
    if self.mode == TRAIN_MODE:
      self.winner = self.population.run(game_runner, AI_GENERATIONS)
      saver = Saver()
      saver.save(self.winner)
    elif self.mode == DISPLAY_MODE:
      self.population.run(game_runner, 1)

  def setup_genome(self, genome, config):
    data = {}
    # Start with fitness level of 0
    genome.fitness = 0
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    data[GENOME] = genome
    data[NET] = net
    self.genome_data.append(data)

  # Initiate the genomes and nn of the birds
  def init_genomes(self, genomes, config) -> None:
    if self.mode == TRAIN_MODE:
      for _, genome in genomes:
        self.setup_genome(genome, config)      
    elif self.mode == DISPLAY_MODE:
      if self.fileDal and self.fileDal.read() == []:
        raise EMPTY_SIMULATION_FILE_ERR

      for genome in self.fileDal.read():
        self.setup_genome(genome, config)

  # Creates an ingame bird for every genome stored
  def init_birds(self, builder: Builder) -> None:
    for data in self.genome_data:
      self.birds.append(IntelligentBird(builder.build_bird(BIRD_INITIAL_X, BIRD_INITAL_Y), data[GENOME], data[NET]))
  
  # Return all game birds
  def get_birds(self) -> List[IntelligentBird]:
    return self.birds

  # Returns if there are inteligent birds
  def has_birds(self) -> bool:
    return len(self.birds) != 0

  def delete_bird(self, bird: IntelligentBird) -> None:
    self.birds.remove(bird)
