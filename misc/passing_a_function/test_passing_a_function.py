import unittest

from passing_a_function import cdr, car, cons


class test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, car(cons(3, 4)))
        self.assertEqual(4, cdr(cons(3, 4)))

        self.assertEqual(4, car(cons(4, 6)))
        self.assertEqual(7, cdr(cons(3, 7)))


if __name__ == "__main__":
    unittest.main()
