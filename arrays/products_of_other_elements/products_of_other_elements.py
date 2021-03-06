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

# O(N) - with division


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

# O(N) - No divison


def multiply_all_others3(arr):
    sums_before = []
    for num in arr:
        if sums_before:
            sums_before.append(sums_before[-1] * num)
        else:
            sums_before.append(num)

    sums_after = []
    for num in reversed(arr):
        if sums_after:
            sums_after.append(sums_after[-1] * num)
        else:
            sums_after.append(num)
    sums_after = list(reversed(sums_after))

    result = []
    for i in range(len(arr)):
        if i == 0:
            result.append(sums_after[i + 1])
        elif i == len(arr) - 1:
            result.append(sums_before[i - 1])
        else:
            result.append(sums_before[i - 1] * sums_after[i + 1])
    return result
