import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.both = 0

    def __str__(self):
        return str(self.val)


class test(unittest.TestCase):
    def test_1(self):
        pass


if __name__ == "__main__":
    unittest.main()
