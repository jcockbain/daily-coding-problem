import unittest

import solution


class test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, solution.longest_substring("abcba", 2))
        self.assertEqual(2, solution.longest_substring("adbid", 2))


if __name__ == "__main__":
    unittest.main()
