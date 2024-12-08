from utils.matrix import Matrix

_start = "S"

_moves = {
    "S" : {},
    "." : {},
    "|" : {
        (1, 0) : (1, 0),
        (-1, 0) : (-1, 0)
    },
    "-" : {
        (0, 1) : (0, 1),
        (0, -1) : (0, -1)
    },
    "L" : {
        (0, -1) : (-1, 0),
        (1, 0): (0, 1)
    },
    "J" : {
        (0, 1) : (-1, 0),
        (1, 0) : (0, -1)
    },
    "7" : {
        (0, 1) : (1, 0),
        (-1, 0) : (0, -1)
    },
    "F" : {
        (0, -1) : (1, 0),
        (-1, 0) : (0, 1)
    }
}

_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class PipeMaze:
    def __init__(self, maze: list[str]):
        self._maze = Matrix(maze, ".")

    def _get_start(self) -> tuple[int, int]:
        for row_id, rows in enumerate(self._maze):
            for col_id, col in enumerate(rows):
                if col == _start:
                    return row_id, col_id

    def _get_loop(self) -> tuple[set[tuple[int, int]], int] :
        y, x = self._get_start()
        moves = list(filter(lambda d:d in _moves[self._maze[(y + d[0], x + d[1])]], _directions))
        cursors = list(zip([(y, x)] * len(moves), moves))
        points = {(y, x)}
        cnt = 0
        looped = False
        while not looped:
            cnt += 1
            new_cursors = []
            for point, direction in cursors:
                nxt = (point[0] + direction[0], point[1] + direction[1])
                if nxt in points:
                    looped = True
                    break
                pipe = self._maze[nxt]
                nxt_direction = _moves[pipe][direction] if direction in _moves[pipe] else (0, 0)
                new_cursors.append((nxt, nxt_direction))
                points.add(nxt)
            cursors = new_cursors
        return points, cnt

    def get_furthest_step(self) -> int:
        _, furthest_step = self._get_loop()
        return furthest_step

    def get_enclosed_tile_count(self) -> int:
        loop, _ = self._get_loop()
        cnt = 0
        return cnt