import pygame

from src.constants import *
from src.display.drawer import Drawer
from src.obj.obj_manager import ObjectManager
from src.obj.pygame_obj_manager import PygameObjectManager
from src.builder import Builder
from src.collision import check_bird_collision


# TODO Remove when implementing the AI
LEFT = 1

# Game loop
def run():
  def run_game_loop():
    global restart
    restart = False

    clock = pygame.time.Clock()

    # Game setup
    obj_manager = ObjectManager()
    pg_obj_manager = PygameObjectManager()
    drawer = Drawer(pg_obj_manager)
    builder = Builder(obj_manager, pg_obj_manager)

    # Here we build the birds
    bird, bird_drawer = builder.build_bird(WIN_WIDTH / 4, WIN_HEIGHT / 2)
    pipes = [ builder.build_pipe(WIN_WIDTH) ]
    base = builder.build_base(FLOOR)

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

      base.move()
      for pipe in pipes:
        pipe.move(bird)
      bird.move()

      if check_bird_collision(bird_drawer, pg_obj_manager):
        restart = True
        break

      if pipes[-1].passed:
        pipes.append(builder.build_pipe(WIN_WIDTH))

      drawer.draw()

  run_game_loop()
  while restart:
    run_game_loop()
