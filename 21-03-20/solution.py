import unittest


def is_sum_1(arr, target):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False


class test(unittest.TestCase):
    def test_find_subsets(self):
        arr = [1, 2, 3, 4]
        arr2 = [2, 4, 6, 10]
        self.assertEqual(is_sum_1(arr, 4), True)
        self.assertEqual(is_sum_1(arr, 12), False)
        self.assertEqual(is_sum_1(arr2, 12), True)
        self.assertEqual(is_sum_1(arr2, 7), False)


if __name__ == "__main__":
    unittest.main()
