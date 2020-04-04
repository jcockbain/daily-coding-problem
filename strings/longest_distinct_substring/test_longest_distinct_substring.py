import unittest

import longest_distinct_substring


class test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            3, longest_distinct_substring.longest_substring("abcba", 2))
        self.assertEqual(
            2, longest_distinct_substring.longest_substring("adbid", 2))


if __name__ == "__main__":
    unittest.main()
