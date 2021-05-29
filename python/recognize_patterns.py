from dataclasses import dataclass
from collections import Counter
import random


# https://stackoverflow.com/a/28875727/14125122

# https://stackoverflow.com/a/38772020/14125122
def patterns(seq):
    storage = {}
    for length in range(1, int(len(seq) / 2) + 1):
        valid_strings = {}
        for start in range(0, len(seq) - length + 1):
            valid_strings[start] = tuple(seq[start:start + length])
        candidates = set(valid_strings.values())
        if len(candidates) != len(valid_strings):
            print("Pattern found for " + str(length))
            storage = valid_strings
        else:
            print("No pattern found for " + str(length))
            break
    return set(v for v in storage.values() if list(storage.values()).count(v) > 1)


# taken from same stackoverflow page as above
def get_pattern(seq):
    seq2 = seq
    outs = {}
    p = 0
    r = 0
    c = None
    for end in range(len(seq2) + 1):
        for start in range(end):
            word = chr(1).join(seq2[start:end])
            if word not in outs:
                outs[word] = 1
            else:
                outs[word] += 1
    for item in outs:
        if outs[item] > r or (len(item) > p and outs[item] > 1):
            p = len(item)
            r = outs[item]
            c = item
    return c.split(chr(1))


@dataclass
class Pattern:
    match: tuple
    count: int
    length: int


def elena_patterns(seq: list, start: int = 2, end: int = None):
    end = end if end is not None else len(seq) >> 1
    patterns = []
    for size in range(start, end):
        found = []
        for sieve in range(len(seq)):
            if len(seq) >= (sieve + size):
                found.append(seq[sieve:(sieve + size)])
        empty = True
        for k, v in Counter((map(tuple, found))).items():
            if v > 1:
                patterns.append(Pattern(k, v, size))
                if empty: empty = False
        if empty:  # this is the best way to stop the loop i could find
            break
    return patterns


if __name__ == '__main__':
    t = [random.randint(0, 10) for _ in range(1000)]
    # t = magic[:-1].split(',')
    # x = elena_patterns(t)
    for x in elena_patterns(t):
        print(x)
