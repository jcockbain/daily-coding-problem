import unittest

# O(N^2)


def first_pos(arr):
    i = 1
    while i <= len(arr) + 1:
        if i not in arr:
            return i
        i += 1
    return 1

# O(N) average case - O(N) Space


def first_pos2(arr):
    s = set(arr)
    i = 1
    while i in s:
        i += 1
    return i
