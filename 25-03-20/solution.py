import unittest


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    return pair(lambda a, b: a)


def cdr(pair):
    return pair(lambda a, b: b)


class test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, car(cons(3, 4)))
        self.assertEqual(4, cdr(cons(3, 4)))

        self.assertEqual(4, car(cons(4, 6)))
        self.assertEqual(7, cdr(cons(3, 7)))


if __name__ == "__main__":
    unittest.main()
