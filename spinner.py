import sys
from itertools import cycle
from threading import Thread
from time import sleep


class Spinner:
    busy = False
    delay = 0.5

    def __init__(self, delay=None):
        # self.spinner = iter(cycle(['-', '\\', '|', '/']))
        # self.spinner = iter(cycle(["🚶 ", "🏃 "]))
        self.spinner = iter(cycle([".  ", ".. ", "...", " ..", "  .", "   "]))
        self.delay = float(delay) if delay else self.delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(f'\r{next(self.spinner)}')
            sleep(self.delay)
            sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        if exception is not None:
            return False


with Spinner():
    for i in range(1, 6):
        sleep(6)
        print(f"\rTask #{i} is done!")
