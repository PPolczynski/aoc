import math
from collections import deque

from utils.matrix import Matrix

_wall = "#"
_adjacent_fields = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Maze:
    def __init__(self, len_x, len_y, falling_bytes: list[str]):
        self._len_x = len_x
        self._len_y = len_y
        self._falling_bytes = [tuple(map(int, f_byte.split(","))) for f_byte in falling_bytes]
        self._start = (0, 0)
        self._end = (len_x - 1, len_y - 1)

    def get_shortest_path_length(self, nano_seconds):
        maze = Matrix.get_empty(self._len_x, self._len_y, ".")
        for t in range(0, nano_seconds):
            maze[self._falling_bytes[t]] = _wall
        points = deque([(0, self._start)])
        visited = set()
        while points:
            length, point = points.pop()
            if (maze.is_out_of_bounds(point)
                    or maze[point] == _wall
                    or point in visited):
                continue
            elif point == self._end:
                return length
            else:
                visited.add(point)
                x, y = point
                for dx, dy in _adjacent_fields:
                    points.appendleft((length + 1, (x + dx, y + dy)))
        return -1

    def get_last_coordinate_before_inescapable(self):
        left = 0
        right = len(self._falling_bytes) - 1
        while left <= right:
            mid = math.floor((left + right) / 2)
            value = self.get_shortest_path_length(mid)
            if value == -1:
                right = mid - 1
            else:
                left = mid + 1
        return self._falling_bytes[left - 1]
