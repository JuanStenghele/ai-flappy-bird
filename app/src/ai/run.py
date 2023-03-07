from src.ai.ai import Ai
from src.ai.setup import *


ai = None
population = None
def run_simulation():
  population = ai_setup()
  ai: Ai = Ai(population)
  ai.add_reporter()
  ai.run_training(run_game)

def run_game(genomes, config):
  print("population")
