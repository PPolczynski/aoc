import re
from dataclasses import dataclass

from puzzle import Solution

lights_re = re.compile(r"\[([.#]+)]")
buttons_re = re.compile(r"\(([\d,]+)\)")
requirements_re = re.compile(r"\{([\d,]+)}")


@dataclass
class Machine:
    target: int
    buttons: list[int]
    requirements: list[int]

    @classmethod
    def from_line(cls, line: str) -> "Machine":
        lights = ["1" if c == "#" else "0" for c in re.findall(lights_re, line)[0][:]]
        l = len(lights)
        buttons = []
        for button_str in re.findall(buttons_re, line):
            b = ["0"] * l
            for n in button_str.split(","):
                b[int(n)] = "1"
            buttons.append(int("".join(b), base=2))
        requirements = [int(n) for n in re.findall(requirements_re, line)[0].split(",")]
        return cls(int("".join(lights), base=2), buttons, requirements)

    def min_presses(self):
        min_press_cnt = len(self.buttons) + 1

        def backtrack(value, idx, press_cnt):
            nonlocal min_press_cnt
            if value == self.target:
                min_press_cnt = min(min_press_cnt, press_cnt)
                return
            elif idx >= len(self.buttons) or press_cnt >= min_press_cnt:
                return
            else:
                backtrack(value ^ self.buttons[idx], idx + 1, press_cnt + 1)
                backtrack(value, idx + 1, press_cnt)

        backtrack(0, 0, 0)
        return min_press_cnt


def _preprocess(data: str) -> list[Machine]:
    return [Machine.from_line(line) for line in data.splitlines()]


def _part1(machines: list[Machine]) -> int:
    m = 0
    for machine in machines:
        m += machine.min_presses()
    return m


def _part2(machines: list[Machine]) -> int:
    return 0


solution = Solution("Factory", "10", "2025",
                    part1=_part1,
                    part2=_part2,
                    part1_preprocess=_preprocess,
                    part2_preprocess=_preprocess)
