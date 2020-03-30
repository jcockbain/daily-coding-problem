import unittest


# O(2^N) time
def maxSum(arr):
    if not arr:
        return 0

    return max(maxSum(arr[1:]), arr[0] + maxSum(arr[2:]))


# O(N) time, O(N) space


def maxSum2(arr):
    if len(arr) <= 2:
        return max(0, max(arr))

    cache = [0 for i in arr]
    cache[0] = max(0, arr[0])
    cache[1] = max(cache[0], arr[1])

    for i in range(2, len(arr)):
        num = arr[i]
        cache[i] = max(num + cache[i - 2], cache[i - 1])
    return cache[-1]


# O(N) time, O(1) space

def maxSum3(arr):
    if len(arr) <= 2:
        return max(0, max(arr))

    max_excluding_last = max(0, arr[0])
    max_including_last = max(max_excluding_last, arr[1])

    for i in arr[2:]:
        prev_max_including_last = max_including_last

        max_including_last = max(max_including_last, max_excluding_last + i)
        max_excluding_last = prev_max_including_last

    return max(max_including_last, max_excluding_last)


class test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(13, maxSum([2, 4, 6, 2, 5]))
        self.assertEqual(10, maxSum([5, 1, 1, 5]))

    def test_2(self):
        self.assertEqual(13, maxSum2([2, 4, 6, 2, 5]))
        self.assertEqual(10, maxSum2([5, 1, 1, 5]))

    def test_3(self):
        self.assertEqual(13, maxSum3([2, 4, 6, 2, 5]))
        self.assertEqual(10, maxSum3([5, 1, 1, 5]))


if __name__ == "__main__":
    unittest.main()
