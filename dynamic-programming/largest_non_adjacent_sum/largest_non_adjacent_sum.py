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
