import unittest

from products_of_other_elements import multiply_all_others, multiply_all_others2, multiply_all_others3


class test(unittest.TestCase):
    def test_mutliply_all_others(self):
        arr1 = [3, 2, 1]
        arr2 = [1, 2, 3, 4, 5]
        arr3 = [0, 3, 5]

        exp1 = [2, 3, 6]
        exp2 = [120, 60, 40, 30, 24]
        exp3 = [15, 0, 0]

        self.assertEqual(multiply_all_others(arr1), exp1)
        self.assertEqual(multiply_all_others(arr2), exp2)
        self.assertEqual(multiply_all_others(arr3), exp3)

        self.assertEqual(multiply_all_others2(arr1), exp1)
        self.assertEqual(multiply_all_others2(arr2), exp2)
        self.assertEqual(multiply_all_others2(arr3), exp3)

        self.assertEqual(multiply_all_others3(arr1), exp1)
        self.assertEqual(multiply_all_others3(arr2), exp2)
        self.assertEqual(multiply_all_others3(arr3), exp3)


if __name__ == "__main__":
    unittest.main()
