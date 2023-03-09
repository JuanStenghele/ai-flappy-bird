import pygame

from src.display.bird_drawer import BirdDrawer
from src.display.pipe_drawer import PipeDrawer
from src.display.base_drawer import BaseDrawer
from src.obj.pygame_obj_manager import PygameObjectManager
from src.obj.bird import Bird
from src.images import PIPE_TOP, PIPE_BOT, BASE_IMG
from src.constants import BIRD_PIPE_COLLISION_TRIGGER, BIRD_BASE_COLLISION_TRIGGER


# Methods for detecting collisions in pygame

TOP_PIPE_MASK = pygame.mask.from_surface(PIPE_TOP)
BOT_PIPE_MASK = pygame.mask.from_surface(PIPE_BOT)
TOP_PIPE_HEIGHT = PIPE_TOP.get_height()
BASE_MASK = pygame.mask.from_surface(BASE_IMG)
  
# Detects any bird collision
def check_bird_collision(bird: Bird, obj_manager: PygameObjectManager) -> bool:
  bird_drawer = obj_manager.get_bird_drawer(bird)

  collides: bool = False
  for pipe in obj_manager.get_pipes_drawers():
    if collision_bird_pipe(bird_drawer, pipe):
      collides = True
      break
  if not collides and collision_bird_base(bird_drawer, obj_manager.get_base_drawer()):
    collides = True
  if not collides and bird.y < -bird_drawer.img.get_height():
    collides = True
  return collides

# Detects a collision between a bird and a pipe
def collision_bird_pipe(bird_drawer: BirdDrawer, pipe_drawer: PipeDrawer) -> bool:
  if abs(pipe_drawer.pipe.x - bird_drawer.bird.x) > BIRD_PIPE_COLLISION_TRIGGER:
    return False

  # First we get the masks
  bird_mask = pygame.mask.from_surface(bird_drawer.img)

  # Now we get the offsets between the pipe and the bird
  top_offset = (pipe_drawer.pipe.x - bird_drawer.bird.x, pipe_drawer.top - TOP_PIPE_HEIGHT - round(bird_drawer.bird.y))
  bot_offset = (pipe_drawer.pipe.x - bird_drawer.bird.x, pipe_drawer.bot - round(bird_drawer.bird.y))

  # Finally we get the overlapping points
  bot_point = bird_mask.overlap(BOT_PIPE_MASK, bot_offset)
  top_point = bird_mask.overlap(TOP_PIPE_MASK, top_offset)

  return bot_point or top_point

# Detects a collision between a bird and a pipe
def collision_bird_base(bird_drawer: BirdDrawer, base_drawer: BaseDrawer) -> bool:
  if base_drawer.base.y - bird_drawer.bird.y > BIRD_BASE_COLLISION_TRIGGER:
    return False

  # First we get the masks
  bird_mask = pygame.mask.from_surface(bird_drawer.img)

  # Now we get the offsets between the pipe and the bird
  offset = (0, bird_drawer.bird.y - base_drawer.base.y)

  # Finally we get the overlapping points
  return BASE_MASK.overlap(bird_mask, offset)
