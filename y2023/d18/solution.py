from dataclasses import dataclass

from puzzle import Solution
from utils.matrix import Matrix

_move_map = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}
_trench = "#"
_empty = "."
_crossing_values = {"F", "7", "|"}
_corners = {
    "U": {
        "R": "F",
        "L": "7",
    },
    "D": {
        "R": "L",
        "L": "J",
    },
    "L": {
        "U": "L",
        "D": "F",
    },
    "R": {
        "U": "J",
        "D": "7",
    }
}
_edges = {
    "U": "|",
    "D": "|",
    "L": "-",
    "R": "-"
}


@dataclass(frozen=True)
class Instruction:
    color: str
    direction: str
    move: tuple[int, int]
    steps: int


def _preprocess(input_data: str) -> list[Instruction]:
    lines = input_data.splitlines()
    instructions = []
    for line in lines:
        direction, steps, color = line.split(" ")
        instructions.append(
            Instruction(
                color[1:-1],
                direction,
                _move_map[direction],
                int(steps)))
    return instructions


def _part1(lines: list[Instruction]) -> any:
    return simulate(lines)


def _part2(lines: list[Instruction]) -> any:
    pass


def simulate(instructions: list[Instruction]):
    x, y = 0, 0
    max_x, max_y = 0, 0
    min_x, min_y = 0, 0
    for ins in instructions:
        dx, dy = ins.move
        x, y = x + (ins.steps * dx), y + (ins.steps * dy)
        max_x, max_y = max(max_x, x), max(max_y, y)
        min_x, min_y = min(min_x, x), min(min_y, y)
    m = Matrix.get_empty(max_x - min_x + 1, max_y - min_y + 1, _empty)

    cnt = 0
    for idx, ins in enumerate(instructions):
        dx, dy = ins.move
        for _ in range(ins.steps):
            x, y = x + dx, y + dy
            m[(x - min_x, y - min_y)] = _edges[ins.direction]
            cnt += 1
        if idx < len(instructions) - 1:
            m[(x - min_x, y - min_y)] = _corners[ins.direction][instructions[idx + 1].direction]
    m[(x - min_x, y - min_y)] = _corners[instructions[-1].direction][instructions[0].direction]

    for i, row in enumerate(m.iterate_row()):
        # https://en.wikipedia.org/wiki/Point_in_polygon
        crossings_count = 0
        for j, v in enumerate(row):
            # we go horizontally so - is not crossing it's going on the edge
            # we could check for pair F 7 or L J
            # L---7 crosses the loop once so we dont want to count L abd 7 just one of them
            # F---7 crosses it twice
            if v in _crossing_values:
                crossings_count += 1
            if v == _empty and crossings_count % 2 != 0:
                cnt += 1
    return cnt


solution = Solution(
    "Lavaduct Lagoon",
    "18",
    "2023",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)
