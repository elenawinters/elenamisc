import colorsys
import discord
import string
import codecs
import math

# valid = string.digits + string.ascii_letters + string.punctuation  # this has the wrong order for letters.
valid = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation

# TODO: NAMES NEED TO BE RENAMED TO BE BETTER


class DiscordColors:
    @classmethod
    def from_hsv(cls, h: int, s: int = 100, v: int = 100):  # Manually parse
        return discord.Color.from_rgb(*tuple(j if j > 0 else 0 for j in (round(i * 255) for i in colorsys.hsv_to_rgb(h / 360, s / 100, v / 100))))


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


class StrBaseConversion:
    def __init__(self, text: str, base: int):
        self.n = text
        self.b = base

    def encode(self) -> str:  # this does cool stuff
        return ''.join(valid[x] for x in ConvertInt2Base(int(self.n.encode('utf8').hex(), 16), self.b).dali())

    def decode(self) -> str:
        return None
        # for x in self.n:
        #     v = valid.index()
        # t = [valid[x] for x in ConvertInt2Base(int(self.n.encode('utf8').hex(), 16), 16).dali()]
        # print(t)
        # return ''.join(valid[x] for x in ConvertInt2Base(int(self.n.encode('utf8').hex(), 16), self.b).dali())


if __name__ == '__main__':  # hsv(199, 19%, 87%) hsv(302, 28%, 92%)
    print(DiscordColors.from_hsv(199, 19, 87))
    # print(valid)
    # print(len(valid))
    # # test = 'The paq member reading this is hella cute. Everyone else is hella cute too though.'
    test = 'no u'
    # print(ConvertStr2Base(test, 16).winters())
    # print(ConvertStr2Base(test, 32).winters())
    base94 = StrBaseConversion(test, 94).encode()
    print(base94)
    print(ROT(base94).s47())

    orig = StrBaseConversion(base94, 94).decode()
    print(orig)
    # print(StrBaseConversion(base94, 94).decode())
    # print(f'{len(base94)} vs hex orig {len(test)*2}')

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
