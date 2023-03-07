from src.ai.setup import *


ai = None

def run_simulation():
  ai = ai_setup()
  ai.run_training()

def run_game(genomes, config):
  print(ai.population)
