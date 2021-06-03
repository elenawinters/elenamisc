import random


class GenerateRandomNumber:
    def __init__(self):
        pass


class GenerateRandomString:
    def __init__(self):
        pass


class GenerateRandomList:
    def __new__(self, limit=6, depth=1):
        self.limit = limit
        self.depth = depth
        self.data = []

        return self.generate()

    def generate(self):
        d_data = []
        for _ in range(self.depth):
            l_data = []
            for _ in range(self.limit):
                pass
        self.data = []


class GenerateRandomDictionary:
    def __new__(self, depth=20, data_limit=20, max_data_length=20):
        self.length = max_data_length
        self.limit = data_limit
        self.depth = depth

        return self.generate()

    def generate(self):
        pass
