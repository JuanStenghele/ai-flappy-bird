import neat

from typing import List
from src.constants import *
from src.obj.builder import Builder
from src.file_dal import FileDal
from src.output import *
from src.ai.saver import Saver
from src.ai.intelligent_bird import IntelligentBird


GENOME = 'genome'
NET = 'net'

# Encapsulates the NEAT Ai
class Ai:
  def __init__(self, config: neat.Config) -> None:
    self.config = config
    self.population = neat.Population(self.config)
    self.winner = None
    self.genome_data = []
    self.birds = []
    self.mode = AiTrainMode(self)

  # Sets display mode
  def set_display_mode(self, simulation_file: str) -> None:
    self.mode = AiDisplayMode(self, simulation_file)

  # Add a stdout reporter to show progress in the terminal.
  def add_reporter(self):
    self.population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    self.population.add_reporter(stats)

  # Runs the game to train the birds
  def run(self, game_runner) -> None:
    self.mode.run(game_runner)
 
  def setup_genome(self, genome):
    data = {}
    self.mode.set_genome_fitness(genome)
    net = neat.nn.FeedForwardNetwork.create(genome, self.config)
    data[GENOME] = genome
    data[NET] = net
    self.genome_data.append(data)

  # Initiate the genomes and nn of the birds
  def init_genomes(self, genomes) -> None:
    self.mode.init_genomes(genomes)

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

  def delete_all_birds(self) -> None:
    self.birds.clear()

  def get_winner(self):
    return self.mode.get_winner()

# Ai mode for training
class AiTrainMode():
  def __init__(self, parent: Ai) -> None:
    self.parent = parent
    self.winner = None

  # Runs the training
  def run(self, game_runner) -> None:
    self.winner = self.parent.population.run(game_runner, AI_GENERATIONS)
    saver = Saver()
    saver.save(self.winner)    

  # Sets genome fitness
  def set_genome_fitness(self, genome) -> None:
    genome.fitness = 0

  # Inits the genomes
  def init_genomes(self, genomes) -> None:
    for _, genome in genomes:
      self.parent.setup_genome(genome)

  # Returns the winner genome
  def get_winner(self):
    return self.winner

# Ai mode for displaying a trined genome
class AiDisplayMode():
  def __init__(self, parent: Ai, simulation_file: str) -> None:
    self.parent = parent
    self.fileDal = FileDal(simulation_file)

  # Runs the display
  def run(self, game_runner) -> None:
    genomes = [data[GENOME] for data in self.parent.genome_data]
    game_runner(genomes, self.parent.config)

  # Sets genome fitness
  def set_genome_fitness(self, _) -> None:
    pass

  # Inits the genomes
  def init_genomes(self, _) -> None:
    if self.fileDal.read() == []:
      raise EMPTY_SIMULATION_FILE_ERR

    for genome in self.fileDal.read():
      self.parent.setup_genome(genome)

  # Returns None
  def get_winner(self):
    return None
