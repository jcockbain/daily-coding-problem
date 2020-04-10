class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def intersection(a, b):
    nodes = set()

    while a is not None:
        nodes.add(a.val)
        a = a.next

    while b is not None:
        if b.val in nodes:
            return b.val
        b = b.next

    return None
