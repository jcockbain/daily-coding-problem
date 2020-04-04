import unittest

from ways_of_climbing_steps import ways, ways2


class test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(5, ways(4))
        self.assertEqual(5, ways2(4))


if __name__ == "__main__":
    unittest.main()
