from src.game import *
from src.ai.run import *
import sys

print('Running AI Flappy Bird')
if len(sys.argv) > 2 and sys.argv[2] == 'train':
    run_simulation(sys.argv[1], True)
else:
    run_simulation(sys.argv[1])

print('Quiting')
