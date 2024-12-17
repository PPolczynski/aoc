import math
import re


class Computer:
    def __init__(self, program: list[str]):
        a,b,c, _, instructions = program
        self._a = int(re.findall("\d+", a)[0])
        self._b = int(re.findall("\d+", b)[0])
        self._c = int(re.findall("\d+", c)[0])
        self._instructions = list(map(int, instructions.split(" ")[1].split(",")))

    def __str__(self):
        return f"A:{self._a}, B:{self._b}, C:{self._c} I: {self._instructions}"

    def run(self) -> str:
        i = 0
        out = []
        while i < len(self._instructions):
            operation = self._instructions[i]
            if operation == 0:
                self._a = math.floor(self._a / (2 ** self.get_combo_operand_value(i)))
            elif operation == 1:
                self._b ^= self._instructions[i + 1]
            elif operation == 2:
                self._b = self.get_combo_operand_value(i) % 8
            elif operation == 3 and self._a != 0:
                i = self._instructions[i + 1]
                continue
            elif operation == 4:
                self._b ^= self._c
            elif operation == 5:
                out.append(str(self.get_combo_operand_value(i) % 8))
            elif operation == 6:
                self._b = math.floor(self._a / (2 ** self.get_combo_operand_value(i)))
            elif operation == 7:
                self._c = math.floor(self._a / (2 ** self.get_combo_operand_value(i)))
            i += 2
        return ",".join(out)

    def get_combo_operand_value(self, i):
        combo = self._instructions[i + 1]
        if 0 <= combo <= 3:
            return combo
        elif combo == 4:
            return self._a
        elif combo == 5:
            return self._b
        elif combo == 6:
            return self._c
        else:
            raise ValueError(f'value {combo} is outside allowed range for combo operand')