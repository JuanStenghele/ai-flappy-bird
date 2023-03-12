import neat

from src.obj.bird import Bird
from src.constants import *


# Class that represents an Ai controlled bird
class IntelligentBird:
  def __init__(self, bird: Bird, genome, net: neat.nn.FeedForwardNetwork) -> None:
    self.bird = bird
    self.genome = genome
    self.net = net

  def jump(self, bird_y: float, next_pipe_top: float, next_pipe_bot: float) -> None:
    output = self.net.activate((bird_y, abs(bird_y - next_pipe_top), abs(bird_y - next_pipe_bot)))
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
