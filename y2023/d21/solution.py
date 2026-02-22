from puzzle import Solution
from utils.matrix import Matrix

_PLOT = "."
_ROCK = "#"
_START = "S"


def _part1(m: Matrix) -> int:
    start = m.find_first(_START)
    m[start] = _PLOT
    steps = 0
    max_steps = 64
    current = [start]
    while len(current) > 0 and steps < max_steps:
        temp = set()
        for c in current:
            for value, possible in m.adjacent(c, include_diagonal=False):
                if value == _ROCK:
                    continue
                else:
                    temp.add(possible)
        steps += 1
        current = list(temp)
    return len(current)


def _part2(m: Matrix) -> int:
    pass


def _preprocess(data) -> Matrix:
    return Matrix(data.splitlines(), _PLOT)


solution = Solution(
    "Step Counter",
    "21",
    "2023",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)
