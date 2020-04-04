import unittest

from monte_carlo_pi import estimate, generate, is_in_circle


class test(unittest.TestCase):
    def test_generate(self):
        self.assertTrue(-1 <= generate()[0] <= 1)
        self.assertTrue(-1 <= generate()[1] <= 1)

    def test_is_in_circle(self):
        self.assertFalse(is_in_circle((2, 1)))
        self.assertTrue(is_in_circle((0.5, 0.5)))

    def test_estimate(self):
        self.assertTrue(3.1 <= estimate(10000) <= 3.2)


if __name__ == "__main__":
    unittest.main()
