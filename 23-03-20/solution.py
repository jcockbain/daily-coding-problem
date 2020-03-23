import unittest

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    pass


def deserialize(node):
    pass



class test(unittest.TestCase):
    def test_serialize(self):


        node = Node('root', Node('left', Node('left.left')), Node('right'))
        res = deserialize(serialize(node)).left.left.val
        self.assertEqual('left.left', res)

if __name__ == "__main__":
    unittest.main()
