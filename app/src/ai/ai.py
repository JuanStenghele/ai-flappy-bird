import neat

from typing import List
from src.constants import *
from src.obj.bird import Bird
from src.builder import Builder


# Class that represents an Ai controlled bird
class IntelligentBird:
  def __init__(self, bird: Bird, genome, net: neat.nn.FeedForwardNetwork) -> None:
    self.bird = bird
    self.genome = genome
    self.net = net

  def jump(self, next_pipe_top: float, next_pipe_bot: float) -> None:
    output = self.net.activate((self.bird.y, abs(self.bird.y - next_pipe_top), abs(self.bird.y - next_pipe_bot)))
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

# Encapsulates the NEAT Ai
class Ai:
  def __init__(self, population: neat.Population) -> None:
    self.population = population
    self.winner = None
    self.genome_data = []
    self.birds = []

  # Add a stdout reporter to show progress in the terminal.
  def add_reporter(self):
    self.population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    self.population.add_reporter(stats)

  # Runs the game to train the birds
  def run_training(self, game_runner) -> None:
    self.winner = self.population.run(game_runner, AI_GENERATIONS)

  # Initiate the genomes and nn of the birds
  def init_genomes(self, genomes, config) -> None:
    # Initiate the genomes and nn
    for _, genome in genomes:
      data = {}
      # Start with fitness level of 0
      genome.fitness = 0
      net = neat.nn.FeedForwardNetwork.create(genome, config)
      data[GENOME] = genome
      data[NET] = net
      self.genome_data.append(data)

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
