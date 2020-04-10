import unittest

from intersection import intersection, LinkedListNode


class test(unittest.TestCase):
    def test_intersection(self):
        root1 = LinkedListNode(3)
        root1.next = LinkedListNode(7)
        root1.next.next = LinkedListNode(8)
        root1.next.next.next = LinkedListNode(10)

        root2 = LinkedListNode(99)
        root2.next = LinkedListNode(1)
        root2.next.next = LinkedListNode(8)
        root2.next.next.next = LinkedListNode(10)

        root3 = LinkedListNode(1)
        root3.next = LinkedListNode(2)

        self.assertEqual(8, intersection(root1, root2))
        self.assertEqual(None, intersection(root1, root3))


if __name__ == "__main__":
    unittest.main()
