import os, neat


# Returns the Ai configuration
def ai_setup() -> neat.Config:
  local_dir = os.path.dirname(__file__)
  config_file = os.path.join(local_dir, 'ai-config.txt')

  config: neat.Config = neat.config.Config(
      neat.DefaultGenome, 
      neat.DefaultReproduction,
      neat.DefaultSpeciesSet, 
      neat.DefaultStagnation,
      config_file
    )

  return config

