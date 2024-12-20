from collections import deque, defaultdict

from utils.matrix import Matrix

_wall = "#"
_start = "S"
_end = "E"
_adjacent_fields = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Maze:
    def __init__(self, maze: list[str], cheat_window: int):
        self._cheat_window = cheat_window
        self._maze = Matrix(maze)

    def _get_path_no_cheating(self):
        start = self._maze.find(_start)[0]
        end = self._maze.find(_end)[0]
        queue = deque([(start, [])])
        shortest = []
        visited = set()
        while queue:
            position, path = queue.popleft()
            if self._maze.is_out_of_bounds(position) or self._maze[position] == _wall or position in visited:
                continue
            elif position == end:
                path.append(end)
                shortest = path
            else:
                x, y = position
                path.append(position)
                visited.add(position)
                for dx, dy in _adjacent_fields:
                    queue.append(((x + dx, y + dy), path.copy()))
        return shortest

    def _cheat(self, start):
        cheats = dict()
        visited = dict()
        queue = deque([(start, 0)])
        while queue:
            position, time_elapsed = queue.popleft()
            if (self._maze.is_out_of_bounds(position)
                    or time_elapsed > self._cheat_window
                    or (position in visited and visited[position] >= time_elapsed)):
                continue
            else:
                x, y = position
                visited[position] = time_elapsed
                if self._maze[position] != _wall:
                    cheats[position] = min(cheats.get(position, float("Inf")), time_elapsed)
                for dx, dy in _adjacent_fields:
                    queue.append(((x + dx, y + dy), time_elapsed + 1))
        return  [(position, time) for position, time in cheats.items()]

    def get_cheats(self):
        path = self._get_path_no_cheating()
        position_distance = dict()
        for distance, point in enumerate(path[::-1]):
            position_distance[point] = distance
        cheats = defaultdict(int)
        for point in path:
            cheat_candidates = self._cheat(point)
            current_distance_left = position_distance[point]
            for position, time in cheat_candidates:
                distance_after_cheat = position_distance[position]
                save = distance_after_cheat - current_distance_left - time
                if save > 0:
                    cheats[save] += 1
        return cheats

    def get_cheats_count(self, saving_at_least: int):
        cheats = self.get_cheats()
        return sum([count if time_saved >= saving_at_least else 0 for time_saved, count in cheats.items()])

