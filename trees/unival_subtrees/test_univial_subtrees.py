import unittest
from univial_subtrees import Node, count_unival


class test(unittest.TestCase):
    def test_1(self):
        root = Node(0)
        root.left = Node(1)
        root.right = Node(0)
        root.right.right = Node(0)
        root.right.left = Node(1)
        root.right.left.left = Node(1)
        root.right.left.right = Node(1)
        self.assertEqual(count_unival(root), 5)

    def test_2(self):
        root2 = Node(1)
        root2.left = Node(1)
        root2.right = Node(0)
        self.assertEqual(count_unival(root2), 2)


if __name__ == "__main__":
    unittest.main()
