import pygame

from typing import List
from src.constants import *
from src.display.drawer import Drawer
from src.obj.obj_manager import ObjectManager
from src.obj.pygame_obj_manager import PygameObjectManager
from src.builder import Builder
from src.remover import Remover
from src.collision import check_bird_collision
from src.ai.ai import Ai, IntelligentBird


LEFT = 1

# Game loop
def run(ai: Ai):
  clock = pygame.time.Clock()

  # Game setup
  obj_manager = ObjectManager()
  pg_obj_manager = PygameObjectManager()
  drawer = Drawer(pg_obj_manager)
  builder = Builder(obj_manager, pg_obj_manager)
  remover = Remover(obj_manager, pg_obj_manager)

  # AI setup
  ai.init_birds(builder)

  # Here we build the game objects
  builder.build_pipe(WIN_WIDTH)
  base = builder.build_base(FLOOR)
  statistics = builder.build_statistics()

  run = True
  while run and ai.has_birds():
    clock.tick(FPS)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()
        break

    if not run:
      break

    birds: List[IntelligentBird] = ai.get_birds()
    pipes = obj_manager.get_pipes()
    # Get info needed for bird movement
    next_pipe = None
    for pipe in pipes:
      if not pipe.passed:
        next_pipe = pipe
        break
    next_pipe_drawer = pg_obj_manager.get_pipe_drawer(next_pipe)
    for bird in birds:
      bird.jump(next_pipe_drawer.top, next_pipe_drawer.bot)
      bird.move()

    # Perform the movements
    base.move()
    pipe_rem = []
    for pipe in pipes:
      pipe.move(bird.get_game_bird())
      if pg_obj_manager.get_pipe_drawer(pipe).is_out_of_screen():
        pipe_rem.append(pipe)
    for pipe in pipe_rem:
      remover.delete_pipe(pipe)

    if pipes[-1].passed:
      for bird in birds:
        bird.reward_score()
      statistics.increase_score()
      builder.build_pipe(WIN_WIDTH)

    drawer.draw()

    # This makes the game too slow
    rem_bird: List[IntelligentBird] = []
    for bird in birds:
      game_bird = bird.get_game_bird()
      if check_bird_collision(game_bird, pg_obj_manager):
        rem_bird.append(bird)
    for bird in rem_bird:
      bird.punish_collision()
      game_bird = bird.get_game_bird()
      remover.delete_bird(game_bird)
      ai.delete_bird(bird)
