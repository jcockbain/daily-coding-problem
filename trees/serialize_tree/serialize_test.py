import unittest
from serialize import serialize, deserialize, Node


class test(unittest.TestCase):
    def test_serialize(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        serialized = 'root left left.left # # # right # #'
        self.assertEqual(serialized, serialize(node))

        res = deserialize(serialize(node)).left.left.val
        self.assertEqual('left.left', res)


if __name__ == "__main__":
    unittest.main()
