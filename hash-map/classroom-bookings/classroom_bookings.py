def minimum_rooms(times):
    if times == []:
        return 0

    d = {}
    for b in times:
        start, end = b
        for m in range(start, end+1):
            if m in d:
                d[m] += 1
            else:
                d[m] = 1

    print(d)

    return max(d.values())
