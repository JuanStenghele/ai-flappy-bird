import pygame

from src.constants import *
from src.display.drawer import Drawer
from src.obj.obj_manager import ObjectManager
from src.obj.bird import Bird


# TODO Remove
LEFT = 1
def run():
  clock = pygame.time.Clock()

  # Game setup
  obj_manager = ObjectManager()
  drawer = Drawer(obj_manager)
  bird = Bird(WIN_WIDTH / 2, WIN_HEIGHT / 2)
  obj_manager.add_bird(bird)

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

    bird.move()

    if run:
      drawer.draw_window()
