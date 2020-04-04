import unittest

from number_of_decodings import decode


class test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, decode('111'))
        self.assertEqual(1, decode('2'))
        self.assertEqual(5, decode('1221'))


if __name__ == "__main__":
    unittest.main()
