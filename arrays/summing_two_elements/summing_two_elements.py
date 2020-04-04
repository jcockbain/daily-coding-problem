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
            looking_for.add(target - a)
    return False
