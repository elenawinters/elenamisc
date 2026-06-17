from dataclasses import dataclass
from collections import Counter
from typing import Union
import random
import time


@dataclass
class Pattern:
    match: tuple
    count: int
    length: int


class PatternTest:
    def __init__(self, sequence: list) -> None:
        self.seq = sequence

    def arun_match(self) -> Union[list, set]:  # https://stackoverflow.com/a/38772020/14125122
        """
            Returns longest matching pattern.
        """
        storage = {}
        for length in range(1, int(len(self.seq) / 2) + 1):
            valid_strings = {}
            for start in range(0, len(self.seq) - length + 1):
                valid_strings[start] = tuple(self.seq[start:start + length])
            candidates = set(valid_strings.values())
            if len(candidates) != len(valid_strings):
                storage = valid_strings
            else:
                break
        return set(v for v in storage.values() if list(storage.values()).count(v) > 1)

    def sieve_of_winters(self, start: int = 2, end: int = None) -> list:
        """
            Made by myself, Elena Winters. Returns all matching patterns within range.
        """
        end = end if end is not None else len(self.seq) >> 1
        patterns = []
        for size in range(start, end):
            found = []
            for sieve in range(len(self.seq)):
                if len(self.seq) >= (sieve + size):
                    found.append(self.seq[sieve:(sieve + size)])
            empty = True
            for k, v in Counter((map(tuple, found))).items():
                if v > 1:
                    patterns.append(Pattern(k, v, size))
                    if empty: empty = False
            if empty:  # this is the best way to stop the loop i could find
                break
        return patterns


class TimeTest:
    def __init__(self, func, iterations=3) -> None:
        self.iterations = iterations
        self.func = func
        self.output = []
        self.times = []

    def run(self, *args, **kwargs) -> tuple:
        """The input function gets run the amount of times specificed plus 1"""
        self.func(*args, **kwargs)  # https://youtu.be/ybh0GttfM8o. First execution is always slower in Python
        for _ in range(self.iterations):
            start = time.perf_counter()
            out = self.func(*args, **kwargs)
            end = time.perf_counter()

            self.times.append(end - start)
            self.output.append(out)

        print([x for x in self.times])
        return tuple(self.output)


if __name__ == '__main__':
    size = 50000

    print('Size of test: ' + str(size))

    sample = [random.randint(0, 10) for _ in range(size)]

    print('\nTime to find all possible patterns:\n')
    TimeTest(PatternTest(sample).sieve_of_winters).run()
