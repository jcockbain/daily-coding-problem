import unittest
from autocomplete import autoComplete1


class test(unittest.TestCase):
    def test_1(self):
        arr = ["dog", "deal", "deer"]
        self.assertEqual(['deal', 'deer'], autoComplete1("de", arr))


if __name__ == "__main__":
    unittest.main()
