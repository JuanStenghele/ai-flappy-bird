from datetime import datetime
from src.file_dal import FileDal

# Class in charge of saving a genome
class Saver:
  def __init__(self, file: str=None) -> None:
    if file is None:
      file_path = f'{datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z")}.bin'
    else:
      file_path = file
    self.file = FileDal(file_path)

  # Saves a genome
  def save(self, genome) -> None:
    self.file.write(genome)
