from collections import deque


def can_walk(board, row, col):
    h, w = len(board), len(board[0])
    if row < 0 or row >= w:
        return False
    if col < 0 or col >= h:
        return False
    return not board[row][col]


def get_valid_neighbours(board, row, col):
    return [(r, c) for r, c in [
        (row, col - 1),
        (row, col + 1),
        (row + 1, col),
        (row - 1, col)
    ]
        if can_walk(board, row, col)
    ]


def find_route(board, start, end):
    h, w = len(board), len(board[0])
    explored = set()
    q = deque([[start]])

    if start == end:
        return 0

    while q:
        path = q.popleft()
        node = path[-1]
        if node not in explored:
            neighbours = [
                p for p in get_valid_neighbours(board, node[0], node[1])
            ]
            for n in neighbours:
                new_path = list(path)
                new_path.append(n)
                q.append(new_path)
                if n == end:
                    return len(new_path) - 1
            explored.add(node)
    return -1
