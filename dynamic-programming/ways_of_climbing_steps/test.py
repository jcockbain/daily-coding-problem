import unittest

import solution


class test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(5, solution.ways(4))
        self.assertEqual(5, solution.ways2(4))

    def test_2(self):
        self.assertEqual(5, solution.ways_general(4))


if __name__ == "__main__":
    unittest.main()
