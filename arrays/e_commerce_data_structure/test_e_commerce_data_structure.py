import unittest

from e_commerce_data_structure import order_array, order_circular_array


class test(unittest.TestCase):
    def test_order_array(self):
        orders = order_array(5)
        orders.record(1)
        orders.record(2)
        self.assertEqual(1, orders.get_last(2))

    def test_order_circular_array(self):
        orders = order_circular_array(5)
        orders.record(1)
        orders.record(2)
        self.assertEqual(1, orders.get_last(2))


if __name__ == "__main__":
    unittest.main()
