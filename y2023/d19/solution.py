import re
from dataclasses import dataclass
from enum import Enum

from puzzle import Solution

_ACCEPT = "A"
_REJECT = "R"
_START = "in"


@dataclass(frozen=True)
class Part:
    x: int
    m: int
    a: int
    s: int

    def __getitem__(self, item: str) -> int:
        if item == "x":
            return self.x
        elif item == "m":
            return self.m
        elif item == "a":
            return self.a
        elif item == "s":
            return self.s
        else:
            raise ValueError("unknown value")

    def sum(self):
        return self.x + self.m + self.a + self.s


class Operation(Enum):
    NONE = 0
    GREATER = 1
    SMALLER = 2


# sb{m<1868:qx,x>2338:kpq,s>1982:jf,hd}
@dataclass(frozen=True)
class Rule:
    field: str
    value: int
    operation: Operation
    outcome: str

    def apply(self, part: Part) -> (bool, str):
        if self.operation == Operation.NONE:
            return True, self.outcome
        part_value = part[self.field]
        if self.operation == Operation.GREATER:
            return part_value > self.value, self.outcome
        else:
            return part_value < self.value, self.outcome


@dataclass(frozen=True)
class Workflow:
    label: str
    rules: list[Rule]

    def resolve(self, part: Part):
        for rule in self.rules:
            terminate, outcome = rule.apply(part)
            if terminate:
                return outcome
        # last rule is always condition less but just in case
        return self.rules[-1].outcome


def _part1(data: tuple[dict[str, Workflow], list[Part]]) -> int:
    workflows, parts = data
    total = 0
    for part in parts:
        label = _START
        labels = [label]
        # print(part)
        while True:
            label = workflows[label].resolve(part)
            labels.append(label)
            if label in {_ACCEPT, _REJECT}:
                break
        # print(" -> ".join(labels))
        if label == _ACCEPT:
            total += part.sum()
    return total


def _part2():
    pass


def _preprocess(data) -> tuple[dict[str, Workflow], list[Part]]:
    workflows_lines, parts_lines = data.split("\n\n")
    parts = []
    for line in parts_lines.splitlines():
        x, m, a, s = re.findall(r"\d+", line)
        parts.append(Part(int(x), int(m), int(a), int(s)))
    workflows = {}
    for line in workflows_lines.splitlines():
        label, rest = line.split("{")
        rules_string = rest[:-1].split(",")
        rules = []
        for rule in rules_string:
            values = re.findall(r"\w+", rule)
            if len(values) == 1:
                rules.append(Rule("", 0, Operation.NONE, values[0]))
            elif len(values) == 3:
                operation = Operation.GREATER if rule.find(">") != -1 else Operation.SMALLER
                field, value, target = values
                rules.append(Rule(field, int(value), operation, target))
            else:
                raise ValueError("malformed rule")
        workflows[label] = Workflow(label, rules)
    return workflows, parts


solution = Solution(
    "Aplenty",
    "19",
    "2023",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)
