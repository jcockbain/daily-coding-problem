def autoComplete1(s, arr):
    results = set()
    for word in arr:
        if word.startswith(s):
            results.add(word)
    res = list(results)
    res.sort()
    return res
