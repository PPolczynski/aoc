import math
from dataclasses import dataclass
from enum import Enum

from puzzle import Solution


class Operation(Enum):
    ADD = "+"
    MULTIPLY = "*"


@dataclass
class Equation:
    values: list[int]
    operation: Operation

    def result(self):
        if self.operation == Operation.ADD:
            return sum(self.values)
        else:
            return math.prod(self.values)

    @classmethod
    def from_lines(cls, lines: list[str], idx_start: int, idx_end: int) -> 'Equation':
        values = [int(line[idx_start:idx_end].strip()) for line in lines[:-1]]
        op = Operation.ADD if lines[-1][idx_start:idx_end].strip() == Operation.ADD.value else Operation.MULTIPLY
        return cls(values, op)


def _preprocess(data: str) -> list[Equation]:
    lines = data.splitlines()
    start_idx = 0
    equations = []
    for idx in range(len(lines[0])):
        if all(line[idx] == " " for line in lines):
            equations.append(Equation.from_lines(lines, start_idx, idx))
            start_idx = idx + 1
    equations.append(Equation.from_lines(lines, start_idx, len(lines[0])))
    return equations


def _part1(equations: list[Equation]) -> int:
    return sum([equation.result() for equation in equations])


def _part2(equations: list[Equation]) -> int:
    pass


solution = Solution("Trash Compactor", "6", "2025",
                    part1=_part1,
                    part2=_part2,
                    part1_preprocess=_preprocess,
                    part2_preprocess=_preprocess)
