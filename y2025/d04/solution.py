from puzzle import Solution
from utils.matrix import Matrix

_ROLL = "@"
_EMPTY = "."
_max_neighbours = 4


def _preprocess(data: str) -> Matrix:
    return Matrix(data.splitlines(), _EMPTY)


def _part1(grid: Matrix) -> int:
    accessible = 0
    for v, c in grid:
        if v == _ROLL:
            cnt = len(list(filter(lambda x: x[0] == _ROLL, grid.adjacent(c, include_diagonal=True))))
            if cnt < _max_neighbours:
                accessible += 1
    return accessible


def _part2(grid: Matrix) -> int:
    graph = dict()

    for v, c in grid:
        if v == _ROLL:
            graph[c] = set()
            for _, n_c in filter(lambda x: x[0] == _ROLL, grid.adjacent(c, include_diagonal=True)):
                graph[c].add(n_c)

    removed = 0
    while True:
        to_remove = list(filter(lambda k: len(graph[k]) < _max_neighbours, graph.keys()))
        for c in to_remove:
            for n_c in graph[c]:
                graph[n_c].remove(c)
            del graph[c]
        if len(to_remove) == 0:
            break
        else:
            removed += len(to_remove)

    return removed


def _part2_brute_force(grid: Matrix) -> int:
    removed = 0
    while True:
        to_remove = set()
        for v, c in grid:
            if v == _ROLL:
                neighbour_rolls = list(filter(lambda x: x[0] == _ROLL, grid.adjacent(c, include_diagonal=True)))
                if len(neighbour_rolls) < _max_neighbours:
                    to_remove.add(c)
        if len(to_remove) == 0:
            break
        else:
            removed += len(to_remove)
            grid.apply(list(to_remove), _EMPTY)
    return removed


solution = Solution("Printing Department ", "4", "2025",
                    part1=_part1,
                    part2=_part2,
                    part1_preprocess=_preprocess,
                    part2_preprocess=_preprocess)
