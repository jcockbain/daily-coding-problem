import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.both = 0

    def __str__(self):
        return str(self.val)


class XORLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

    def add(self, element):
        node = Node(element)
        current = this.head
        if self.head.val == None:
            self.head = self.tail = node
        else:
            node.both = get_pointer(self.tail)
            self.tail.both = self.tail.both ^


class test(unittest.TestCase):
    def test_1(self):
        xor = XORLinkedList()


if __name__ == "__main__":
    unittest.main()
