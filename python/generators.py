from timetest import TimeTest
import typing
import random
import string


class GenerateRandomBoolean:
    def __new__(cls):
        return bool(random.getrandbits(1))


class GenerateRandomNumber:
    def __new__(cls, max=1000000):
        match random.choice(['int', 'float']):
            case 'float':
                return random.randint(0.0, float(max))
            case 'int':
                return random.randint(0, int(max))


class GenerateRandomString:
    def __new__(cls, length=20):
        return ''.join([random.choice(string.ascii_letters) for _ in range(random.randint(length >> 1, length))])


# Convert to use this https://realpython.com/introduction-to-python-generators/
class GenerateRandomList:  # SUFFERS FROM RECURSION LIMIT
    def __new__(cls, limit=20, sublist_limit=1):
        cls.sublist_limit = sublist_limit if sublist_limit <= 400 else 400
        cls.limit = limit
        cls.sublists = 1

        cls.options = [GenerateRandomString, GenerateRandomNumber, cls.generate_list]

        return cls.depth_loop()
        # return cls.data

    @classmethod
    def depth_loop(cls):
        data = []
        for _ in range(random.randint(cls.limit >> 1, cls.limit)):
            data.append(random.choice([*cls.options])())
        return data

    @classmethod
    def generate_list(cls):
        if cls.sublists < cls.sublist_limit:
            cls.sublists += 1
            return cls.depth_loop()
        else:
            return GenerateRandomBoolean()


class GenerateRandomDictionary:
    def __new__(cls, depth=20, data_limit=20, max_data_length=20):
        cls.length = max_data_length
        cls.limit = data_limit
        cls.depth = depth
        cls.data = {}

        cls.generate()
        return cls.data

    def generate(cls):
        pass


if __name__ == '__main__':
    # list_times = TimeTest(GenerateRandomList, 1).run(limit=400, sublist_limit=400)
    # print('Time to randomly generate lists:\n' + str([x.elapsed for x in list_times]), end='\n\n')
    # contents = list_times[0].returned
    # print(len(contents))
    print(GenerateRandomList(sublist_limit=400))
    # print([GenerateRandomList() for _ in range(50)])
    # print([GenerateRandomNumber() for _ in range(50)])
