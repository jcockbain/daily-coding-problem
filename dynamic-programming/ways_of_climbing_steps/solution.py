def ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return ways(n-2) + ways(n-1)


def ways2(n):
    cache = [0] * n
    cache[0] = 1
    cache[1] = 2
    for i in range(2, n):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[-1]
