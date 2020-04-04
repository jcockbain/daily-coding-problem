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
