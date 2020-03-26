import unittest

# O(N^2)


def first_pos(arr):
    i = 1
    while i <= len(arr) + 1:
        if i not in arr:
            return i
        i += 1
    return None

# O(N) average case - O(N) Space


def first_pos2(arr):
    s = set(arr)
    i = 1
    while i in s:
        i + 1
    return i


class test(unittest.TestCase):
    def test_first_pos2(self):
        self.assertEqual(2, first_pos([3, 4, 1, -2]))
        self.assertEqual(5, first_pos([1, 2, 3, 4]))
        self.assertEqual(2, first_pos([3, 4, 1, -2]))

        self.assertEqual(2, first_pos2([3, 4, 1, -2]))
        self.assertEqual(5, first_pos2([1, 2, 3, 4]))
        self.assertEqual(2, first_pos2([3, 4, 1, -2]))


if __name__ == "__main__":
    unittest.main()
