from unittest import TestCase

from y2023.d18.solution import Instruction, _preprocess


class Test(TestCase):
    def test__preprocess(self):
        self.assertListEqual(_preprocess("U 2 (#caa173)"), [Instruction("#caa173", "U", (0, -1), 2)])
        self.assertListEqual(_preprocess("L 1 (#1b58a2)\nU 2 (#caa171)"),
                             [Instruction("#1b58a2", "L", (-1, 0), 1), Instruction("#caa171", "U", (0, -1), 2)])
