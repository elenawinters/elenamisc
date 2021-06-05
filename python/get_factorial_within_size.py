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

    def calculate(self) -> Factorial:
        for formula in range(1, self.size + 4):  # for loop is technically faster than a while loop
            _num = self.calc_factorial(formula + 1)
            if len(str(_num)) > self.size:
                self.factorial = formula
                break
            self.answer = _num
        return Factorial(self.factorial, self.answer, len(str(self.answer)))


# TODO: Move this to generators.py
if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(GetFactorialOfLength(int(sys.argv[1])).calculate())
    else:
        size = 5000
        print(f'Time for ~{size}!')
        TimeTest(GetFactorialOfLength(size).calculate).run()
        # print(f'\n{TimeTest(GetFactorialOfLength(size).calculate).run()[0]}\n')
