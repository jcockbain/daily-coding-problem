def longest_substring(s, k):
    current_longest = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if len(set(substring)) <= k and len(substring) > len(current_longest):
                current_longest = substring
    return len(current_longest)
