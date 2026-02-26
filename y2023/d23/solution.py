import copy
import heapq
import math
from dataclasses import dataclass

from puzzle import Solution
from utils.matrix import Matrix

_EMPTY = "."
_ROCK = "#"

_slope_move = {
    ">": (1, 0),
    "<": (-1, 0),
    "v": (0, 1),
    "^": (0, -1),
}

_slopes = set(_slope_move.keys())


def _part1(m: Matrix) -> int:
    start = (1, 0)
    end = (m.len_x - 2, m.len_y - 1)
    longest = 0
    paths = [(0, start, {start})]
    while len(paths) > 0:
        l, coord, seen = paths.pop()
        if coord == end:
            longest = max(l, longest)
            continue
        for n_v, n_c in m.adjacent(coord):
            if n_c in seen or n_v == _ROCK:
                continue
            elif n_v in _slopes:
                dx, dy = n_c[0] - coord[0], n_c[1] - coord[1]
                if (dx, dy) == _slope_move[n_v]:
                    s2 = seen.copy()
                    s2.add(n_c)
                    paths.append((l + 1, n_c, s2))
            else:
                s2 = seen.copy()
                s2.add(n_c)
                paths.append((l + 1, n_c, s2))
    return longest


@dataclass
class Node:
    coordinate: tuple[int, int]
    connections: set[(int, tuple[int, int])]


def _part2(m: Matrix) -> int:
    start = (1, 0)
    end = (m.len_x - 2, m.len_y - 1)
    graph = dict()
    graph[start] = Node(start, set())
    paths = [(point[1], graph[start]) for point in list(filter(lambda adj: adj[0] != _ROCK, m.adjacent(start)))]
    while len(paths) > 0:
        point, start_node = paths.pop()
        seen = {start_node.coordinate, point}
        steps = 0
        while True:
            candidates = list(filter(lambda adj: adj[0] != _ROCK and adj[1] not in seen, m.adjacent(point)))
            if len(candidates) == 0:  # this would mean it's a loop shouldn't happen
                raise RuntimeError("I was wrong it did happened. Loop?")
            elif len(candidates) == 1:
                steps += 1
                point = candidates[0][1]
                seen.add(point)
                if point == end:
                    break
                else:
                    continue
            else:
                break
        if point not in graph:
            graph[point] = Node(point, set())
        else:
            candidates = []
        n = graph[point]
        start_node.connections.add((point, steps))
        n.connections.add((start_node.coordinate, steps))
        for _, c in candidates:
            paths.append((c, n))

    longest = 0
    paths = [(0, start, {start})]
    while len(paths) > 0:
        l, coord, seen = paths.pop()
        node = graph[coord]
        if coord == end:
            longest = max(l - 1, longest)
            continue
        for n_c, d in node.connections:
            if n_c in seen:
                continue
            else:
                s2 = seen.copy()
                s2.add(n_c)
                paths.append((l + d + 1, n_c, s2))
    return longest


def _preprocess(data) -> Matrix:
    return Matrix(data.splitlines(), _EMPTY)


solution = Solution(
    "A Long Walk",
    "23",
    "2023",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)
