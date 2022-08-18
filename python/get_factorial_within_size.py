from dataclasses import dataclass
from testutils import TimeTest
import sys


@dataclass
class Factorial:
    formula: int = 0
    result: int = 0
    length: int = 0


class GetFactorialOfLength:
    def __init__(self, size) -> None:
        self.size = size
        self.answer = 1
        self.last = 1

    def calc_factorial(self, n) -> int:
        if n < 1:
            return 1
        self.last = self.last * n
        return self.last

    def calculate_loop(self) -> Factorial:  # Loop method is significantly faster than Generator method in tests
        for formula in range(1, self.size + 4):
            _num = self.calc_factorial(formula + 1)
            if len(str(_num)) > self.size:
                self.factorial = formula
                break
            self.answer = _num
        return Factorial(self.factorial, self.answer, len(str(self.answer)))

    def calc_generator(self):
        stored = 1
        for formula in range(1, self.size * 5):
            generated = stored * formula
            if len(str(generated)) > self.size:
                yield stored, len(str(stored)), formula - 1
            stored = generated

    def calculate_gen(self) -> Factorial:
        for number, length, factorial in self.calc_generator():
            return Factorial(factorial, number, length)


# TODO: Move this to generators.py
# Well, I've learned that generators are slow.
if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(GetFactorialOfLength(int(sys.argv[1])).calculate_gen())
    else:
        size = 5000
        print(f'Time for ~{size}! For-Loop')
        TimeTest(GetFactorialOfLength(size).calculate_loop).run()
        # print(GetFactorialOfLength(size).calculate_loop())
        print(f'Time for ~{size}! Generator')
        TimeTest(GetFactorialOfLength(size).calculate_gen).run()
        # print(GetFactorialOfLength(size).calculate_gen())
        # print(f'\n{TimeTest(GetFactorialOfLength(size).calculate).run()[0]}\n')
