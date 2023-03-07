import neat

from src.constants import *


# Encapsulates the NEAT Ai
class Ai:
  def __init__(self, population: neat.Population) -> None:
    self.population = population
    self.winner = None

  # Add a stdout reporter to show progress in the terminal.
  def add_reporter(self):
    self.population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    self.population.add_reporter(stats)

  # Runs the game to train the birds
  def run_training(self, run_game):
    self.winner = self.population.run(run_game, AI_GENERATIONS)

