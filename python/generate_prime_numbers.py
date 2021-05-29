# The goal of this is to experiment with generating prime numbers fast without error.
# This is almost certainly impossible but I wanna try my hand at it

import recognize_patterns
import ast


class GeneratePrimeNumbers:
    def __init__(self, limit=0):
        self.limit = limit
        self.primes = []

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

    # def sieve_of_eratosthenes(self):
    #     prime = [True for i in range(2, self.limit)]
    #     for num in range(2, self.limit):

    def filter_primes(self):  # this is slow
        return list(filter(self.is_prime, range(2, self.limit)))

    def check_differences(self, primes):  # this doesn't calculate primes really.... i mean it does it just checks for differences
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
        self.primes.append(2)
        for x in range(3, self.limit):
            if not self.is_odd(x):
                continue

            if self.is_prime(x):
                self.primes.append(x)
        return self.primes


if __name__ == '__main__':
    pattern_algo = recognize_patterns.elena_patterns
    # (6, 14, 4, 26, 4, 2, 12, 10, 8, 4, 8, 12, 4)  # 5132 pattern, same for 9591
    calc = False
    if calc:
        size = 50000
        primes = GeneratePrimeNumbers(size).elena_skip()
        diff = GeneratePrimeNumbers().check_differences(primes)
        with open(f'{len(primes)}_primes.txt', 'w') as file:
            file.write(str(primes))

        with open(f'{len(diff)}_primes_diff.txt', 'w') as file:
            file.write(str(diff))

        pattern = pattern_algo(diff)
        print(pattern)

        with open(f'{len(diff)}_pattern_match.txt', 'w') as file:
            for x in pattern:
                file.write(f'{x}\n')

    else:
        test_sequence = 9591
        data = []
        with open(f'{test_sequence}_primes_diff.txt') as file:
            data = ast.literal_eval(file.read())

        pattern = pattern_algo(data)
        print(pattern)

        with open(f'{test_sequence}_pattern_match.txt', 'w') as file:
            for x in pattern:
                file.write(f'{x}\n')

    # output = GeneratePrimeNumbers().check_differences(GeneratePrimeNumbers(50000).elena_skip())
    # output = GeneratePrimeNumbers(50000).elena_skip()
    # size = len(output)
    # with open(f'{size}_primes_diff.txt', 'w') as file:
    #     file.write(str(output))
    # print(GeneratePrimeNumbers(50000).elena_skip())
    # output = GeneratePrimeNumbers(10000).check_differences()
    # print(output)
    # pattern = recognize_patterns.pattern(output)
    # print(pattern)
