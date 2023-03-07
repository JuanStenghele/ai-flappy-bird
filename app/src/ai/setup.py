import os, neat


# Returns a configured Ai
def ai_setup() -> neat.Population:
  local_dir = os.path.dirname(__file__)
  config_file = os.path.join(local_dir, 'ai-config.txt')

  config: neat.Config = neat.config.Config(
      neat.DefaultGenome, 
      neat.DefaultReproduction,
      neat.DefaultSpeciesSet, 
      neat.DefaultStagnation,
      config_file
    )

  # Create the population, which is the top-level object for a NEAT run.
  population: neat.Population = neat.Population(config)


  return population
