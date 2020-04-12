import unittest

from traverse_matrix import find_route


class test(unittest.TestCase):
    def setUp(self):
        self.board = [[False, False, False, False],
                      [True, True, False, True],
                      [False, False, False, False],
                      [False, False, False, False]]

    def test_find_route_1(self):
        self.assertEqual(7, find_route(self.board, (3, 0), (0, 0)))

    def test_find_route_2(self):
        self.assertEqual(5, find_route(self.board, (2, 1), (0, 0)))

    def test_find_route_3(self):
        self.assertEqual(6, find_route(self.board, (0, 0), (2, 0)))


if __name__ == "__main__":
    unittest.main()
