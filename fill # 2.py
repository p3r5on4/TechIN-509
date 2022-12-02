from typing import List

g = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
##define the moves up down left right
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    seen = set()
##sets up board dimension according to index
    height = len(board)
    width = len(board[0])

    def spread(i, j):
        if not 0 <= i < height or not 0 <= j < width or (i, j) in seen or board[i][j] != old:
            return
        seen.add((i, j))

        board[i] = board[i][:j] + new + board[i][j + 1 :]
        for p, q in directions:
            spread(i + p, j + q)

    spread(x, y)

    return board


ans = flood_fill(g, ".", "~", 2, 10)

for a in ans:
    print(a)