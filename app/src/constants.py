import pygame.font

# Display
WIN_WIDTH = 480
WIN_HEIGHT = 720

# Fonts
pygame.font.init()
STAT_FONT = pygame.font.SysFont("comicsans", 30)

# Game
GAME_NAME = 'Flappy Bird'
FPS = 30
GRAVITY = 3
LOSE_FREEZE = 2

# Pipe
PIPE_GAP = 200
PIPE_SPEED = 5

# BASE
FLOOR = 650  # TODO check this depending on windows
BASE_SPEED = 96

# Bird
BIRD_JUMP_SPEED = -10.5
BIRD_MAX_SPEED_DOWN = 30.0
BIRD_ANIM_TRANSITION_TICKS = 5
BIRD_MAX_ROT = 30
BIRD_MIN_ROT = -90
BIRD_ROT_SPEED = 15
BIRD_DIVING_ROT = -80

# AI
AI_GENERATIONS = 50
