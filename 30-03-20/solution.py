import unittest


def jobScheduler(f, n):
    return f


if __name__ == "__main__":
    print(jobScheduler((lambda x: x+1)(2), 1000))
