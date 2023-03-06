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
  if not collides and collision_bird_base(bird, obj_manager.get_base_drawer()):
    collides = True
  return collides

# Detects a collision between a bird and a pipe
def collision_bird_pipe(bird_drawer: BirdDrawer, pipe_drawer: PipeDrawer) -> bool:
  # First we get the masks
  bird_mask = pygame.mask.from_surface(bird_drawer.img)
  top_pipe_mask = pygame.mask.from_surface(pipe_drawer.PIPE_TOP)
  bot_pipe_mask = pygame.mask.from_surface(pipe_drawer.PIPE_BOT)

  # Now we get the offsets between the pipe and the bird
  top_offset = (pipe_drawer.pipe.x - bird_drawer.bird.x, pipe_drawer.top - round(bird_drawer.bird.y))
  bot_offset = (pipe_drawer.pipe.x - bird_drawer.bird.x, pipe_drawer.bot - round(bird_drawer.bird.y))

  # Finally we get the overlapping points
  bot_point = bird_mask.overlap(bot_pipe_mask, bot_offset)
  top_point = bird_mask.overlap(top_pipe_mask, top_offset)

  return bot_point or top_point

# Detects a collision between a bird and a pipe
def collision_bird_base(bird_drawer: BirdDrawer, base_drawer: BaseDrawer) -> bool:
  # First we get the masks
  bird_mask = pygame.mask.from_surface(bird_drawer.img)
  base_mask = pygame.mask.from_surface(base_drawer.img)

  # Now we get the offsets between the pipe and the bird
  offset = (0, bird_drawer.bird.y - base_drawer.base.y)

  # Finally we get the overlapping points
  return base_mask.overlap(bird_mask, offset)
