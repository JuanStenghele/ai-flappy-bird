from src.ai.ai import Ai
from src.ai.setup import *
from src.game import run

def run_simulation():
  population = ai_setup()
  global ai
  ai = Ai(population)
  ai.add_reporter()
  ai.run_training(game_runner)

def game_runner(genomes, config):
  ai.init_genomes(genomes, config)
  run(ai)
