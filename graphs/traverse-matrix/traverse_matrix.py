from collections import deque


def get_neighbours(position):
    x, y = position
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]


def find_route(board, start, end):
    h, w = len(board), len(board[0])
    no_gates = set()
    for r in range(h):
        for c in range(w):
            if not board[r][c]:
                no_gates.add((r, c))

    explored = set()
    q = [[start]]

    if start == end:
        return 0

    while q:
        path = q.pop(0)
        node = path[-1]
        if node not in explored:
            all_neighbours = get_neighbours(node)
            neighbours = [
                p for p in all_neighbours if p in no_gates and 0 <= p[0] <= h and 0 <= p[1] <= w]
            for n in neighbours:
                new_path = list(path)
                new_path.append(n)
                q.append(new_path)
                if n == end:
                    return len(new_path) - 1
            explored.add(node)
    return -1
