import heapq
from utils.matrix import Matrix

_start = "S"
_end = "E"
_wall = "#"
_start_direction = (1, 0)
_adjacent_fields = [(-1, 0), (0, 1), (1, 0), (0, -1)]
_move_cost = 1
_rotation_cost = 1000

class Maze:
    def __init__(self, maze: list[str]):
        self._maze = Matrix(maze, _wall)
        self._source = maze

    def race(self) -> tuple[int,list[set]]:
        direction = _start_direction
        start = self._maze.find(_start)[0]
        candidates = [(0, start, direction, set())]
        heapq.heapify(candidates)
        visited = dict()
        lowest_score = float("Inf")
        winner_paths = []
        while candidates:
            score, coordinate, direction_facing, path = heapq.heappop(candidates)
            key = (coordinate, direction_facing)
            if self._maze[coordinate] == _end:
                if lowest_score == score:
                    winner_paths.append(path)
                elif lowest_score > score:
                    winner_paths = [path]
                    lowest_score = score
            elif (key in visited and visited[key] < score) or lowest_score < score :
                continue
            x, y = coordinate
            fx, fy = direction_facing
            visited[key] = score
            path.add(coordinate)
            directions = list(filter(lambda d: self._maze[(x + d[0], y + d[1])] != _wall, _adjacent_fields))
            for dx, dy in directions:
                candidate_score = score
                if fx == dx and fy == dy:
                    candidate_score += _move_cost
                else:
                    candidate_score += _move_cost + _rotation_cost * 1 if abs(fx) != abs(dx) else 2
                if candidate_score <= lowest_score:
                    heapq.heappush(candidates, (candidate_score, (x + dx, y + dy), (dx, dy), path.copy()))
        all_paths = set()
        for path in winner_paths:
            all_paths |= path
            # empty = Matrix(self._source)
            # for point in path:
            #     empty[point] = "0"
            # print(empty)
            # print("")
        return lowest_score, all_paths
