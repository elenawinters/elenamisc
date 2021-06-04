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


# Convert to use this https://realpython.com/introduction-to-python-generators/ at some point
class GenerateRandomList:  # SUFFERS FROM RECURSION LIMIT
    def __new__(cls, limit=20, sublist_limit=2):
        cls.sublist_limit = sublist_limit if sublist_limit <= 400 else 400
        cls.limit = limit
        cls.sublists = 0

        cls.options = [GenerateRandomString, GenerateRandomNumber, cls.generate_list]

        return cls.depth_loop()
        # return cls.data

    @classmethod
    def depth_loop(cls):
        data = []
        for _ in range(random.randint(cls.limit >> 1, cls.limit)):
            data.append(random.choice([*cls.options])(random.randint(cls.limit >> 1, cls.limit << 1)))
        return data

    @classmethod
    def generate_list(cls, _):
        if cls.sublists < cls.sublist_limit:
            cls.sublists += 1
            return cls.depth_loop()
        else:
            return GenerateRandomBoolean()


# # This uses same method as above. Needs to be converted to another method
# class GenerateRandomDictionary:
#     def __new__(cls, limit=20, subdict_limit=20):
#         cls.subdict_limit = subdict_limit if subdict_limit <= 400 else 400
#         cls.limit = limit
#         cls.subdicts = 0

#         cls.options = [GenerateRandomString, GenerateRandomNumber, GenerateRandomList, cls.generate_dict]

#         cls.generate_dict(typing.Any)
#         return cls.data

#     @classmethod
#     def depth_loop(cls):
#         data = {}
#         for _ in range(random.randint(cls.limit >> 1, cls.limit)):
#             data.update(random.choice([*cls.options])(random.randint(cls.limit >> 1, cls.limit)))
#         return data

#     @classmethod
#     def generate_dict(cls, _):
#         if cls.subdicts < cls.subdict_limit:
#             cls.subdicts += 1
#             return cls.depth_loop()
#         else:
#             return GenerateRandomBoolean()


if __name__ == '__main__':
    print(TimeTest(GenerateRandomList, 3).run(limit=10))
    # print('Time to randomly generate lists:\n' + str([x.elapsed for x in list_times]), end='\n\n')
    # contents = list_times[0].returned
    # print(len(contents))
    # print(GenerateRandomList())
    # print([GenerateRandomList() for _ in range(50)])
    # print([GenerateRandomNumber() for _ in range(50)])
