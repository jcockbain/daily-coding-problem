import unittest

from classroom_bookings import minimum_rooms


class test(unittest.TestCase):
    def test_bookings(self):
        times = [(30, 75), (0, 50), (60, 150)]
        self.assertEqual(2, minimum_rooms(times))

        times2 = [(30, 75), (0, 50), (60, 150), (0, 65)]
        self.assertEqual(3, minimum_rooms(times2))

        times3 = [(30, 75), (80, 100), (110, 150)]
        self.assertEqual(1, minimum_rooms(times3))

        times4 = [(0, 100), (0, 100), (100, 200)]
        self.assertEqual(3, minimum_rooms(times4))

        self.assertEqual(0, minimum_rooms([]))


if __name__ == "__main__":
    unittest.main()
