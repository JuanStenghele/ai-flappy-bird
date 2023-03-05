import pygame

from src.constants import *
from src.display.drawer import Drawer
from src.obj.obj_manager import ObjectManager
from src.obj.pygame_obj_manager import PygameObjectManager
from src.obj.bird_builder import BirdBuilder
from src.obj.pipe_builder import PipeBuilder


# TODO Remove when implementing the AI
LEFT = 1
# Game loop
def run():
  clock = pygame.time.Clock()

  # Game setup
  obj_manager = ObjectManager()
  pg_obj_manager = PygameObjectManager()
  drawer = Drawer(pg_obj_manager)
  bird_builder = BirdBuilder(obj_manager, pg_obj_manager)
  pipe_builder = PipeBuilder(obj_manager, pg_obj_manager)

  # Here we build the birds
  bird = bird_builder.build(WIN_WIDTH / 4, WIN_HEIGHT / 2)
  pipe_builder.build(WIN_WIDTH)

  run = True
  while run:
    clock.tick(FPS)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()
        break
      elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
        bird.jump()

    if not run:
      break

    bird.move()

    drawer.draw()
