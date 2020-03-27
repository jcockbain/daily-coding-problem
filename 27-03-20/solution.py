import unittest


def decode(s):
    if not s or s[0] == '0':
        return 0

    dp = [0 for x in range(len(s) + 1)]

    dp[0:2] = [1, 1]

    for i in range(2, len(s) + 1):
        if 0 < int(s[i-1:i]) <= 9:
            dp[i] += dp[i-1]
        if 10 < int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]

    return dp[-1]


class test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, decode('111'))
        self.assertEqual(1, decode('2'))
        self.assertEqual(5, decode('1221'))


if __name__ == "__main__":
    unittest.main()
