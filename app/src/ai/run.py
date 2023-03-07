from src.ai.ai import Ai
from src.ai.setup import *
from src.game import run

ai = None
population = None
def run_simulation():
  population = ai_setup()
  ai: Ai = Ai(population)
  ai.add_reporter()
  ai.run_training(run_game)

def run_game(genomes, config):
  run(genomes, config)
