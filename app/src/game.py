from src.flappy_bird import FlappyBird
from src.ai.ai import Ai

# Game loop
def run(ai: Ai):
  game = FlappyBird(ai)
  game.run()
