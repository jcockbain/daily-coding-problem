class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    vals = []

    def encode(node):
        if node:
            vals.append(str(node.val))
            encode(node.left)
            encode(node.right)
        else:
            vals.append('#')
    encode(node)
    return ' '.join(vals)


def deserialize(vals):
    def decode(vals):
        val = next(vals)
        if val == "#":
            return None
        node = Node(val)
        node.left = decode(vals)
        node.right = decode(vals)
        return node

    vals = iter(vals.split())
    return decode(vals)


