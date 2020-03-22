import unittest

# O(N^2)


def multiply_all_others(arr):
    result = [0] * len(arr)
    for i in range(len(arr)):
        v = 1
        for j in range(len(arr)):
            if j != i:
                v *= arr[j]
        result[i] = v
    return result

# O(N)


def multiply_all_others2(arr):
    result = []
    total = product(arr)
    for i in range(len(arr)):
        if arr[i] == 0:
            result.append(product(remove_element(arr, i)))
        else:
            result.append(total / arr[i])
    return result


def product(arr):
    result = 1
    for a in arr:
        result *= a
    return result


def remove_element(arr, i):
    return arr[:i] + arr[i + 1:]


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


if __name__ == "__main__":
    unittest.main()
