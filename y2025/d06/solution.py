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

    @classmethod
    def from_lines_by_columns(cls, lines: list[str], idx_start: int, idx_end: int) -> 'Equation':
        values = []
        for idx in range(idx_start, idx_end):
            v = 0
            for line in lines[:-1]:
                if line[idx] != " ":
                    v *= 10
                    v += int(line[idx])
            values.append(v)
        op = Operation.ADD if lines[-1][idx_start:idx_end].strip() == Operation.ADD.value else Operation.MULTIPLY
        return cls(values, op)


def _preprocess(equation_factory):
    def fn(data: str):
        lines = data.splitlines()
        start_idx = 0
        equations = []
        for idx in range(len(lines[0])):
            if all(line[idx] == " " for line in lines):
                equations.append(equation_factory(lines, start_idx, idx))
                start_idx = idx + 1
        equations.append(equation_factory(lines, start_idx, len(lines[0])))
        return equations

    return fn


def _part1(equations: list[Equation]) -> int:
    return sum([equation.result() for equation in equations])


solution = Solution("Trash Compactor", "6", "2025",
                    part1=_part1,
                    part2=_part1,
                    part1_preprocess=_preprocess(Equation.from_lines),
                    part2_preprocess=_preprocess(Equation.from_lines_by_columns))
