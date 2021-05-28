from dataclasses import dataclass
import sys


@dataclass
class Factorial:
    formula: int = 0
    result: int = 0
    length: int = 0


class GetFactorialOfLength:
    def __init__(self, size):
        self.factorial = 1
        self.size = size
        self.answer = 0
        self.last = 1

    def calc_factorial(self, n):
        if n < 1:
            return 1
        self.last = self.last * n
        return self.last

    def calculate(self):
        while True:
            _num = self.calc_factorial(self.factorial + 1)
            if len(str(_num)) > self.size:
                break
            self.factorial += 1
            self.answer = _num
        return Factorial(self.factorial, self.answer, len(str(self.answer)))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(GetFactorialOfLength(int(sys.argv[1])).calculate())
    else:
        while True:
            size = int(input('Specify Size of Factorial Number: '))
            out = GetFactorialOfLength(size).calculate()
            print('')
            print(f'Factorial: {out.formula}!', end='\n\n')
            print(f'Length: {out.length}', end='\n\n')
            print(f'Result:\n{out.result}', end='\n\n')

