import unittest

from summing_two_elements import can_make_target1, can_make_target2


class test(unittest.TestCase):
    def test_find_subsets(self):
        arr = [1, 2, 3, 4]
        arr2 = [2, 4, 6, 10]

        self.assertEqual(can_make_target1(arr, 4), True)
        self.assertEqual(can_make_target1(arr, 12), False)
        self.assertEqual(can_make_target1(arr2, 12), True)
        self.assertEqual(can_make_target1(arr2, 7), False)

        self.assertEqual(can_make_target2(arr, 4), True)
        self.assertEqual(can_make_target2(arr, 12), False)
        self.assertEqual(can_make_target2(arr2, 12), True)
        self.assertEqual(can_make_target2(arr2, 7), False)


if __name__ == "__main__":
    unittest.main()
