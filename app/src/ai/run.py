from src.ai.ai import Ai
from src.ai.setup import *
from src.game import run
from src.output import *


def run_simulation(simulation_file: str = None):
  config = ai_setup()
  global ai
  ai = Ai(config)
  if simulation_file:
    ai.set_display_mode(simulation_file)
  else:
    ai.add_reporter()
  ai.run(game_runner)
  winner = ai.get_winner()
  if winner is not None:
    print(BEST_GENOME.format(winner))

def game_runner(genomes, _):
  ai.init_genomes(genomes)
  run(ai)
