from src.ai.ai import Ai
from src.ai.setup import *
from src.game import run
from src.output import *


def run_simulation(simulation_file: str = None):
  population = ai_setup()
  global ai
  ai = Ai(population)
  if simulation_file:
    ai.set_display_mode(simulation_file)
  else:
    ai.add_reporter()
  ai.run(game_runner)
  print(BEST_GENOME.format(ai.winner))

def game_runner(genomes, config):
  ai.init_genomes(genomes, config)
  run(ai)
