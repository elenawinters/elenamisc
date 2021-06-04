import time


class TimeTest:
    def __init__(self, func, iterations=1):
        self.iterations = iterations
        self.func = func
        self.output = []
        self.times = []

    def run(self, *args, **kwargs):
        for _ in range(self.iterations):
            start = time.perf_counter()
            out = self.func(*args, **kwargs)
            end = time.perf_counter()

            self.times.append(end - start)
            self.output.append(out)

        print([x for x in self.times])
        return tuple(self.output)
