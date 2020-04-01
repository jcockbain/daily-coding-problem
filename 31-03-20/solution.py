import unittest


def autoComplete1(s, arr):
    results = set()
    for word in arr:
        if word.startswith(s):
            results.add(word)
    return list(results)


class test(unittest.TestCase):
    def test_1(self):
        arr = ["dog", "deer", "deal"]
        self.assertListEqual(['deer', 'deal'], autoComplete1("de", arr))


if __name__ == "__main__":
    unittest.main()
