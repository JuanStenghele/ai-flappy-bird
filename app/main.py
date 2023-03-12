from src.game import *
from src.ai.run import *
import sys

print('Running AI Flappy Bird')
if (len(sys.argv) > 1):
  run_simulation(sys.argv[1])
else:
  run_simulation()
print('Quiting')
