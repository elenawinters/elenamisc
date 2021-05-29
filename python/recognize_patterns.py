from dataclasses import dataclass
from collections import Counter
from timetest import TimeTest
import random


@dataclass
class Pattern:
    match: tuple
    count: int
    length: int


class PatternMatching:
    def __init__(self, sequence: list = []):
        self.seq = sequence

    def arun_match(self):
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

    def sieve_of_winters(self, start: int = 2, end: int = None):
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


if __name__ == '__main__':
    size = 500

    print('Size of test: ' + str(size), end='\n\n')

    t = [random.randint(0, 10) for _ in range(size)]

    pattern_times = TimeTest(PatternMatching(t).sieve_of_winters, 3).run()
    print('Time to find all possible patterns:\n' + str([x.elapsed for x in pattern_times]), end='\n\n')
