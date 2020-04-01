import time
import threading
import unittest


class Scheduler:
    def __init__(self):
        self.fns = []  # tuple of (fn, time)
        t = threading.Thread(target=self.poll)
        t.start()

    def poll(self):
        while True:
            now = time.time() * 1000
            for fn, due in self.fns:
                if now > due:
                    fn()
            self.fns = [(fn, due) for (fn, due) in self.fns if due > now]
            time.sleep(0.01)

    def delay(self, f, n):
        self.fns.append((f, time.time() * 1000 + n))


if __name__ == "__main__":
    s = Scheduler()
    s.delay(lambda: print('4'), 1000)
