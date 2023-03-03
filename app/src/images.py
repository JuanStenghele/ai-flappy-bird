import os
import pygame

from src.constants import *


IMAGE_PATH = 'app/res/img'

def load_image(path: str) -> pygame.Surface:
    return pygame.image.load(os.path.join(IMAGE_PATH, path))

PIPE_IMG = pygame.transform.scale2x(load_image('pipe.png')).convert_alpha()
BG_IMG = pygame.transform.scale(load_image('bg.png').convert_alpha(), (WIN_WIDTH, WIN_HEIGHT))
BIRD_IMGS = [pygame.transform.scale2x(load_image(f'bird{str(x)}.png')) for x in range(1,4)]
BASE_IMG = pygame.transform.scale2x(load_image('base.png').convert_alpha())
