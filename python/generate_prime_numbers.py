# The goal of this is to experiment with generating prime numbers fast without error.
# This is almost certainly impossible but I wanna try my hand at it

from recognize_patterns import PatternMatching
from timetest import TimeTest
import math
import sys
import ast


class GeneratePrimeNumbers:
    def __init__(self, limit=0):
        self.limit = limit

    def is_odd(self, number):
        if number % 2:
            return True
        return False

    def is_prime(self, number):
        if number == 0 or number == 1:
            return False
        for i in range(2, int(number >> 1) + 1):
            if (number % i) == 0:
                return False
        else:
            return True

    # https://gist.github.com/mineta/7840849
    def sieve_of_atkin(self):
        primes = []
        is_prime = dict([(i, False) for i in range(5, self.limit + 1)])
        for x in range(1, int(math.sqrt(self.limit)) + 1):
            for y in range(1, int(math.sqrt(self.limit)) + 1):
                n = 4 * x**2 + y**2
                if (n <= self.limit) and ((n % 12 == 1) or (n % 12 == 5)):
                    is_prime[n] = not is_prime[n]
                n = 3 * x**2 + y**2
                if (n <= self.limit) and (n % 12 == 7):
                    is_prime[n] = not is_prime[n]
                n = 3 * x**2 - y**2
                if (x > y) and (n <= self.limit) and (n % 12 == 11):
                    is_prime[n] = not is_prime[n]
        for n in range(5, int(math.sqrt(self.limit)) + 1):
            if is_prime[n]:
                ik = 1
                while (ik * n**2 <= self.limit):
                    is_prime[ik * n**2] = False
                    ik += 1
        for i in range(self.limit + 1):
            if i in [0, 1, 4]: pass
            elif i in [2, 3] or is_prime[i]: primes.append(i)
            else: pass
        return primes

    def filter_primes(self):  # this is slow
        return list(filter(self.is_prime, range(2, self.limit)))

    def check_differences(self, primes):  # this doesn't calculate primes really.... it just checks for differences
        diff = []
        last = 0
        for x in primes:
            if not last:
                last = x
            else:
                diff.append(x - last)
                last = x
        return diff

    def elena_skip(self):
        primes = [2]
        for x in range(3, self.limit):
            if not self.is_odd(x):
                continue

            if self.is_prime(x):
                primes.append(x)
        return primes


if __name__ == '__main__':
    size = 500000

    print('Size of test: ' + str(size))

    print('\nTime for primes to be generated:\n')
    primes = TimeTest(GeneratePrimeNumbers(size).sieve_of_atkin, 3).run()[0]

    print('\nTime for differences to be calculated:\n')
    diff = TimeTest(GeneratePrimeNumbers().check_differences, 3).run(primes)[0]

    print('\nTime to find all possible patterns:\n')
    TimeTest(PatternMatching(diff).sieve_of_winters, 3).run()
