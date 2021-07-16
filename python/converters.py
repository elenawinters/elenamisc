import string
import codecs

# valid = string.digits + string.ascii_letters + string.punctuation  # this has the wrong order for letters.
valid = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation

# TODO: NAMES NEED TO BE RENAMED TO BE BETTER


class ROT:  # s for both, c for encode, u for decode
    def __init__(self, text: str):
        self.s = text

    def s47(self) -> str:
        x = []
        for i in range(len(self.s)):
            j = ord(self.s[i])
            if 33 <= j <= 126:
                x.append(chr(33 + ((j + 14) % 94)))
            else:
                x.append(self.s[i])
        return ''.join(x)

    def s13(self) -> str:
        return codecs.encode(self.s, 'rot13')


class ConvertInt2Base:
    def __init__(self, number: int, base: int):
        self.n = number
        self.b = base

    def martelli(self) -> str:  # https://stackoverflow.com/a/2267446/14125122
        n = self.n if type(self.n) == int else int(self.n)
        if self.b > len(valid): return 'Requested base exceeds character list!'
        if n < 0:
            sign = -1
        elif n == 0:
            return valid[0]
        else:
            sign = 1

        n *= sign
        digits = []

        while n:
            digits.append(valid[int(n % self.b)])
            n = int(n / self.b)

        if sign < 0:
            digits.append('-')

        digits.reverse()

        return ''.join(digits)

    def dali(self) -> str:  # https://stackoverflow.com/a/28666223/14125122
        n = int(self.n)
        b = self.b
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        return digits[::-1]


class ConvertStr2Base:
    def __init__(self, text: str, base: int):
        self.n = text
        self.b = base

    def winters(self) -> str:  # this does cool stuff
        return ''.join(valid[x] for x in ConvertInt2Base(int(self.n.encode('utf8').hex(), 16), self.b).dali())


if __name__ == '__main__':
    print(valid)
    print(len(valid))
    test = 'This is a test string. Nothing to find here.'
    print(ConvertStr2Base(test, 16).winters())
    print(ConvertStr2Base(test, 32).winters())
    base94 = ConvertStr2Base(test, 94).winters()
    print(base94)
    print(ROT(base94).s47())
    print(f'{len(base94)} vs hex orig {len(test)*2}')

    # base94 = BaseConverter(valid)
    # print(base94.encode(test))
    # print(ConvertInt2Base(test, 16).martelli())
    # print(ConvertInt2Base(int(test.encode('utf8').hex(), 16), 32).dali())
    # print(ConvertInt2Base('9' * 10, 16).martelli())
    # print(ConvertInt2Base('9' * 10, 32).martelli())
    # print(ConvertInt2Base('9' * 10, 94).martelli())
    # print(ConvertInt2Base('9' * 10, 16).dali())
    # print(ConvertInt2Base('9' * 10, 32).dali())
    # print(ConvertInt2Base('9' * 10, 94).dali())
