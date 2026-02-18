import time
from collections import defaultdict
from utils.matrix import Matrix
from puzzle import Solution


_wall = "#"
_start = "S"
_end = "E"
_adjacent_fields = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def _preprocess(input_data: str) -> list[str]:
    return input_data.splitlines()

def _part1(lines: list[str]) -> any:
    maze = Maze(lines, 2)
    return maze.get_cheats_count(100)

def _part2(lines: list[str]) -> any:
    maze = Maze(lines, 20)
    return maze.get_cheats_count(100)

solution = Solution(
    "Race Condition",
    "20",
    "2024",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)

def get_grid(start: tuple[int, int], distance: int):
    grid = []
    x, y = start
    for y_offset in range(-distance, distance + 1):
        for x_offset in range(-distance + abs(y_offset), distance - abs(y_offset) + 1):
           grid.append((x + x_offset, y  + y_offset))
    return grid

class Maze:
    def __init__(self, maze: list[str], cheat_window: int):
        self._cheat_window = cheat_window
        self._maze = Matrix(maze)

    def _get_path_no_cheating(self):
        start = self._maze.find(_start)[0]
        queue = [start]
        path = [] #there is only one path in this maze
        visited = set()
        while queue:
            position = queue.pop()
            if self._maze.is_out_of_bounds(position) or self._maze[position] == _wall or position in visited:
                continue
            elif self._maze[position] == _end:
                path.append(position)
                break
            else:
                x, y = position
                path.append(position)
                visited.add(position)
                for dx, dy in _adjacent_fields:
                    queue.append((x + dx, y + dy))
        return path

    def _cheat(self, start, position_distance,saving_at_least):
        current_distance_left = position_distance[start]
        x, y = start
        cheats = defaultdict(int)
        for point in get_grid(start, self._cheat_window):
            if not self._maze.is_out_of_bounds(point) and self._maze[point] != _wall:
                distance_after_cheat = position_distance[point]
                distance = abs(x - point[0]) + abs(y - point[1])
                save = distance_after_cheat - current_distance_left - distance
                if save >= saving_at_least:
                    cheats[save] += 1
        return cheats

    def get_cheats(self, saving_at_least):
        path = self._get_path_no_cheating()
        position_distance = dict()
        for distance, point in enumerate(path[::-1]):
            position_distance[point] = distance
        cheats = defaultdict(int)
        for point in path:
            found_cheats = self._cheat(point, position_distance, saving_at_least)
            for key, value in found_cheats.items():
                cheats[key] += value
        return cheats

    def get_cheats_count(self, saving_at_least: int):
        cheats = self.get_cheats(saving_at_least)
        return sum([count for _, count in cheats.items()])
