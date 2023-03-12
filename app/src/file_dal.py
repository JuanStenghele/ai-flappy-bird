import pickle


class FileDal:
  def __init__(self, file_path):
    self.file_path = file_path

  def read(self):
    try:
      with open(self.file_path, 'rb') as f:
        try:
          return pickle.load(f)
        except EOFError:
          return []
    except OSError:
      return[]

  def write(self, new_content):
    if self.read() == []:
      content = [new_content]
    else:
      content = self.read()
      content.append(new_content)
    with open(self.file_path, 'wb') as f:
      pickle.dump(content, f, pickle.HIGHEST_PROTOCOL)
