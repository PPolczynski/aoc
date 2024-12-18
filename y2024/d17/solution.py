import math
import re

_octal = 8

class Computer:
    def __init__(self, program: list[str]):
        a,b,c, _, instructions = program
        self._a = int(re.findall("\d+", a)[0])
        self._b = int(re.findall("\d+", b)[0])
        self._c = int(re.findall("\d+", c)[0])
        self._instructions = list(map(int, instructions.split(" ")[1].split(",")))

    def __str__(self):
        return f"A:{self._a}, B:{self._b}, C:{self._c} I: {self._instructions}"

    def run(self) -> list[int]:
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
                out.append(self.get_combo_operand_value(i) % 8)
            elif operation == 6:
                self._b = math.floor(self._a / (2 ** self.get_combo_operand_value(i)))
            elif operation == 7:
                self._c = math.floor(self._a / (2 ** self.get_combo_operand_value(i)))
            i += 2
        return out

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

    def run_for(self, a, b, c) -> list[int]:
        self._a = a
        self._b = b
        self._c = c
        return self.run()

    def get_a_returning_copy(self):
        result = set()
        current = [0] * len(self._instructions)
        for r in range(_octal):
            current[0] = r
            result |= self.brute_force(current, 0)
        return sorted(list(result))

    def brute_force(self, current, idx):
        output = self.run_for(int("".join(map(str, current)), _octal), 0, 0)
        if self._instructions == output:
            return {int("".join(map(str, current)), _octal)}
        elif (idx < len(current) - 1
              and len(self._instructions) == len(output)
              and self._instructions[len(self._instructions) - idx:] == output[len(output) - idx:]):
            out = set()
            for r in range(_octal):
                current[idx + 1] = r
                out |= self.brute_force(current, idx + 1)
            current[idx+ 1] = 0
            return out
        return set()
