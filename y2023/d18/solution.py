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
_hex_to_direction = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U"
}


@dataclass(frozen=True)
class Instruction:
    direction: str
    move: tuple[int, int]
    steps: int


def _preprocess(input_data: str) -> list[Instruction]:
    lines = input_data.splitlines()
    instructions = []
    for line in lines:
        direction, steps, _ = line.split(" ")
        instructions.append(
            Instruction(
                direction,
                _move_map[direction],
                int(steps)))
    return instructions


def _preprocess_part_2(input_data: str) -> list[Instruction]:
    lines = input_data.splitlines()
    instructions = []
    for line in lines:
        _, _, color = line.split(" ")
        v = color[2:-1]
        steps = int(v[:-1], 16)
        direction = _hex_to_direction[v[-1:]]
        instructions.append(
            Instruction(
                direction,
                _move_map[direction],
                int(steps)))
    return instructions


def _part1(lines: list[Instruction]) -> any:
    return simulate(lines)


def _part2(instructions: list[Instruction]) -> any:
    x, y = 0, 0
    points = [(x, y)]
    bounds = 0
    for ins in instructions:
        dx, dy = ins.move
        x, y = x + (ins.steps * dx), y + (ins.steps * dy)
        bounds += ins.steps
        points.append((x, y))

    # https://en.wikipedia.org/wiki/Shoelace_formula
    area = 0
    for idx, point in enumerate(points):
        x, y = point
        # for the last point the next one is first
        next_y = points[idx + 1][1] if idx + 1 < len(points) else points[0][1]
        # for the first the previous point is last -1 wraps us to last element of list
        previous_y = points[idx - 1][1]
        area += x * (next_y - previous_y)
    area = abs(area) // 2
    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    inside = area - bounds // 2 + 1
    return inside + bounds


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
    part2_preprocess=_preprocess_part_2
)
