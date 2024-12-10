from utils.matrix import Matrix

_start = "S"

_moves = {
    "S" : {},
    "." : {},
    "|" : {
        (0, 1) : (0, 1),
        (0, -1) : (0, -1)
    },
    "-" : {
        (1, 0) : (1, 0),
        (-1, 0) : (-1, 0)
    },
    "L" : {
        (-1, 0) : (0, -1),
        (0, 1): (1, 0)
    },
    "J" : {
        (1, 0) : (0, -1),
        (0, 1) : (-1, 0)
    },
    "7" : {
        (1, 0) : (0, 1),
        (0, -1) : (-1, 0)
    },
    "F" : {
        (-1, 0) : (0, 1),
        (0, -1) : (1, 0)
    }
}

_inside = {
    (0, -1) : (1, 0),
    (0, 1) : (0, 0),
    (1, 0) : (0, 0),
    (-1, 0) : (0, 0)
}

_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
_empty_field = "."

class PipeMaze:
    def __init__(self, maze: list[str]):
        self._maze = Matrix(maze, _empty_field)

    def _get_start(self) -> tuple[int, int]:
        for value, coordinates in self._maze:
            if value == _start:
                return coordinates

    def _get_loop(self) -> tuple[set[tuple[int, int]], int] :
        x, y = self._get_start()
        moves = list(filter(lambda d:d in _moves[self._maze[(x + d[0], y + d[1])]], _directions))
        cursors = list(zip([(x, y)] * len(moves), moves))
        points = {(x, y)}
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

    def get_start_pipe(self):
        x, y = self._get_start()
        moves = list(filter(lambda d: d in _moves[self._maze[(x + d[0], y + d[1])]], _directions))
        for pipe in _moves.keys():
            values = set(_moves[pipe].values())
            if all([move in values for move in moves]):
                return pipe, (x, y)

    def get_enclosed_tile_count(self) -> int:
        loop, _ = self._get_loop()
        pipe, start = self.get_start_pipe()
        self._maze[start] = pipe
        total = 0
        for value, point in self._maze:
            if point not in loop:
                crossings_count = self._cast_ray(point, loop)
                total += crossings_count % 2
        self._maze[start] = _start
        return total

    # https://en.wikipedia.org/wiki/Point_in_polygon
    def _cast_ray(self, from_point: tuple[int, int], polygon: set) -> int:
        crossings_count = 0
        dx, dy = (1, 0)
        x, y = from_point
        # we go horizontally so - is not crossing it's going on the brode
        # we could check for pair F 7 or L J
        # L---7 crosses the loop once so we dont want to count L abd 7 just one of them
        # F---7 crosses it twice
        crossing_values = {"F", "7", "|"}
        while not self._maze.is_out_of_bounds((x, y)):
            crossings_count += 1 \
                if ((x, y) in polygon and self._maze[(x, y)]
                    in crossing_values) else 0
            x, y = x + dx, y + dy
        return crossings_count
