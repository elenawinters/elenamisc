from dataclasses import dataclass
import time


@dataclass(frozen=True)
class TimeTestResults:
    returned: str
    elapsed: int


class TimeTest:
    def __init__(self, func, iterations=1):
        self.iterations = iterations
        self.func = func
        self.tests = []

    def run(self, *args, **kwargs):
        for _ in range(self.iterations):
            start = time.perf_counter()
            out = self.func(*args, **kwargs)
            end = time.perf_counter()

            self.tests.append(TimeTestResults(out, end - start))

        return self.tests
