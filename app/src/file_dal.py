import pickle


class FileDal:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'rb') as f:
            try:
                return pickle.load(f)
            except EOFError:
                return []


    def write(self, new_content):
        if self.read() == []:
            print(11)
            content = [self.read(), new_content]
        else:
            print(22)
            content = [new_content]
        print("LEN", len(content))
        for item in content:
            print(item)
        with open(self.file_path, 'wb') as f:
            pickle.dump(content, f, pickle.HIGHEST_PROTOCOL)
