import largest_non_adjacent_sum
import unittest


class test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(13, largest_non_adjacent_sum.maxSum([2, 4, 6, 2, 5]))
        self.assertEqual(10, largest_non_adjacent_sum.maxSum([5, 1, 1, 5]))

    def test_2(self):
        self.assertEqual(13, largest_non_adjacent_sum.maxSum2([2, 4, 6, 2, 5]))
        self.assertEqual(10, largest_non_adjacent_sum.maxSum2([5, 1, 1, 5]))

    def test_3(self):
        self.assertEqual(13, largest_non_adjacent_sum.maxSum3([2, 4, 6, 2, 5]))
        self.assertEqual(10, largest_non_adjacent_sum.maxSum3([5, 1, 1, 5]))


if __name__ == "__main__":
    unittest.main()
