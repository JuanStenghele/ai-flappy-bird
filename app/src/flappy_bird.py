import pygame

from src.display.drawer import Drawer
from src.constants import *
from src.obj.obj_manager import ObjectManager
from src.obj.pygame_obj_manager import PygameObjectManager
from src.obj.builder import Builder
from src.obj.remover import Remover
from src.ai.ai import Ai, IntelligentBird
from typing import List
from src.collision import check_bird_collision


LEFT = 1

# Game class
class FlappyBird:
  def __init__(self, ai: Ai = None) -> None:
    self.init_game(ai)

  # Inits all the game variables
  def init_game(self, ai: Ai = None) -> None:
    # Game setup
    self.obj_manager = ObjectManager()
    self.pg_obj_manager = PygameObjectManager()
    self.drawer = Drawer(self.pg_obj_manager)
    self.builder = Builder(self.obj_manager, self.pg_obj_manager)
    self.remover = Remover(self.obj_manager, self.pg_obj_manager)

    self.clock = pygame.time.Clock()

    # AI setup
    self.ai = ai
    self.ai.init_birds(self.builder)

    # Here we build the first game objects
    self.builder.build_pipe(WIN_WIDTH)
    self.base = self.builder.build_base(FLOOR)
    self.statistics = self.builder.build_statistics()

  # Runs the game
  def run(self) -> None:
    # Game loop
    run = True
    while run and self.ai.has_birds():
      self.clock.tick(FPS)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
          pygame.quit()
          quit()
        elif event.type == pygame.KEYDOWN:
          # Skip the generation with the R key pressed
          if event.key == pygame.K_r:
            run = False
            break

      if not run:
        break

      # Birds movement
      self.move_birds()

      # Base movement
      self.base.move()

      # Pipe movement
      self.move_pipes()

      # Update game score if necessary 
      self.update_score()

      # Draw every sprite
      self.drawer.draw()

      # Check collisions between birds and pipes or base
      self.check_collisions()

    self.ai.delete_all_birds()


  # Moves all the birds
  def move_birds(self):
    birds: List[IntelligentBird] = self.ai.get_birds()
    pipes = self.obj_manager.get_pipes()
    # Get info needed for bird movement
    next_pipe = None
    for pipe in pipes:
      if not pipe.passed:
        next_pipe = pipe
        break
    next_pipe_drawer = self.pg_obj_manager.get_pipe_drawer(next_pipe)
    for bird in birds:
      bird_drawer = self.pg_obj_manager.get_bird_drawer(bird.get_game_bird())
      # Bird movement
      bird.move()
      bird.jump(bird_drawer.get_mask_center_y(), next_pipe_drawer.top, next_pipe_drawer.bot)

  # Moves all the pipes
  def move_pipes(self):
    pipes = self.obj_manager.get_pipes()
    pipe_rem = []
    for pipe in pipes:
      pipe.move()
      pipe_drawer = self.pg_obj_manager.get_pipe_drawer(pipe)
      pipe_drawer.update_passed()
      if pipe_drawer.is_out_of_screen():
        pipe_rem.append(pipe)
    for pipe in pipe_rem:
      self.remover.delete_pipe(pipe)

  # Adds a point and a new pipe if necessary
  def update_score(self):
    birds: List[IntelligentBird] = self.ai.get_birds()
    pipes = self.obj_manager.get_pipes()
    if pipes[-1].passed:
      for bird in birds:
        bird.reward_score()
      self.statistics.increase_score()
      self.builder.build_pipe(WIN_WIDTH)

  # Checks if any bird collides any pipe or the base and kills it
  def check_collisions(self):
    birds: List[IntelligentBird] = self.ai.get_birds()
    rem_bird: List[IntelligentBird] = []
    for bird in birds:
      game_bird = bird.get_game_bird()
      if check_bird_collision(game_bird, self.pg_obj_manager):
        rem_bird.append(bird)
    for bird in rem_bird:
      bird.punish_collision()
      game_bird = bird.get_game_bird()
      self.remover.delete_bird(game_bird)
      self.ai.delete_bird(bird)
