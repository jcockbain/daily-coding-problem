import unittest

import first_missing_positive


class test(unittest.TestCase):
    def test_first_pos1(self):
        self.assertEqual(2, first_missing_positive.first_pos([3, 4, 1, -2]))
        self.assertEqual(5, first_missing_positive.first_pos([1, 2, 3, 4]))
        self.assertEqual(2, first_missing_positive.first_pos([3, 4, 1, -2]))

    def test_first_pos2(self):
        self.assertEqual(2, first_missing_positive.first_pos2([3, 4, 1, -2]))
        self.assertEqual(5, first_missing_positive.first_pos2([1, 2, 3, 4]))
        self.assertEqual(2, first_missing_positive.first_pos2([3, 4, 1, -2]))


if __name__ == "__main__":
    unittest.main()
