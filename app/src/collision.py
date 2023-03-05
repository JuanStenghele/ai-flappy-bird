import pygame

from src.display.bird_drawer import BirdDrawer
from src.display.pipe_drawer import PipeDrawer
from src.display.base_drawer import BaseDrawer
from src.obj.pygame_obj_manager import PygameObjectManager


# Methods for detecting collisions in pygame

# Detects any bird collision
def check_bird_collision(bird: BirdDrawer, obj_manager: PygameObjectManager) -> bool:
  collides: bool = False
  for pipe in obj_manager.get_pipes_drawers():
    if collision_bird_pipe(bird, pipe):
      collides = True
      break
  return collides

# Detects a collision between a bird and a pipe
def collision_bird_pipe(bird: BirdDrawer, pipe: PipeDrawer) -> bool:
  # First we get the masks
  bird_mask = pygame.mask.from_surface(bird.img)
  top_pipe_mask = pygame.mask.from_surface(pipe.PIPE_TOP)
  bot_pipe_mask = pygame.mask.from_surface(pipe.PIPE_BOT)

  # Now we get the offsets between the pipe and the bird
  top_offset = (pipe.pipe.x - bird.bird.x, pipe.top - round(bird.bird.y))
  bot_offset = (pipe.pipe.x - bird.bird.x, pipe.bot - round(bird.bird.y))

  # Finally we get the overlapping points
  bot_point = bird_mask.overlap(bot_pipe_mask, bot_offset)
  top_point = bird_mask.overlap(top_pipe_mask, top_offset)

  return bot_point or top_point
