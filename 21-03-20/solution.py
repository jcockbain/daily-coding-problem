import unittest

# O(N^2)


def can_make_target1(arr, target):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False

# O(N)


def can_make_target2(arr, target):
    looking_for = set()
    for a in arr:
        if a in looking_for:
            return True
        else:
            looking_for.append(target - a)
    return False


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
