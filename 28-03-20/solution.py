import unittest


class Node(object):

    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


def count_unival(root):
    count = 0

    def traverse(node):
        nonlocal count
        if node.left is None and node.right is None:
            count += 1
        elif node.left.val == node.right.val:
            count += 1
        if node.left:
            traverse(node.left)
        if node.right:
            traverse(node.right)

    traverse(root)
    return count


def printTree(node):
    if node.left:
        printTree(node.left)
    print(node.val)
    if node.right:
        printTree(node.right)


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
