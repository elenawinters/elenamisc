import configparser
import os


class ConfigManager(configparser.ConfigParser):
    def __init__(self, file='config.ini'):
        self.config = super()
        self.file = file
        self.read()

    def read(self):
        if os.path.exists(self.file):
            self.config.read(self.file)
        else:
            return 'File not found'

    def save(self):
        try:
            with open(self.file, 'w') as file:
                self.config.write(file)
        except Exception as exc:
            for _ in range(3):
                print(exc)

    def write(self):
        self.save()


config = ConfigManager()


if __name__ == '__main__':
    print(config.read())
