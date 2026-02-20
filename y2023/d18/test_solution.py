from unittest import TestCase

from y2023.d18.solution import Instruction, _preprocess, _preprocess_part_2


class Test(TestCase):
    def test__preprocess(self):
        self.assertListEqual(_preprocess("U 2 (#caa173)"), [Instruction("U", (0, -1), 2)])
        self.assertListEqual(_preprocess("L 1 (#1b58a2)\nU 2 (#caa171)"),
                             [Instruction("L", (-1, 0), 1), Instruction("U", (0, -1), 2)])

    def test__preprocess_part_2(self):
        self.assertListEqual(_preprocess_part_2("U 2 (#caa173)"), [Instruction("U", (0, -1), 829975)])
        self.assertListEqual(_preprocess_part_2("L 1 (#1b58a2)\nU 2 (#caa171)"),
                             [Instruction("L", (-1, 0), 112010), Instruction("D", (0, 1), 829975)])
