from unittest import TestCase

from y2025.d01.solution import Rotation


class TestRotation(TestCase):
    def test_from_line(self):
        self.assertEqual(Rotation(-1, 68), Rotation.from_line("L68"))
        self.assertEqual(Rotation(1, 48), Rotation.from_line("R48"))
        self.assertEqual(Rotation(-1, 1), Rotation.from_line("L1"))
        self.assertEqual(Rotation(-1, 0), Rotation.from_line("L100"))
        self.assertEqual(Rotation(1, 0), Rotation.from_line("R100"))
        self.assertEqual(Rotation(-1, 1), Rotation.from_line("L101"))
        self.assertEqual(Rotation(-1, 99), Rotation.from_line("L199"))

    def test_position_after(self):
        position = 50
        self.assertEqual(82, Rotation.from_line("L68").position_after(position))
        position = 82
        self.assertEqual(52, Rotation.from_line("L30").position_after(position))
        position = 52
        self.assertEqual(0, Rotation.from_line("R48").position_after(position))
        position = 0
        self.assertEqual(95, Rotation.from_line("L5").position_after(position))
        position = 95
        self.assertEqual(55, Rotation.from_line("R60").position_after(position))
        position = 55
        self.assertEqual(0, Rotation.from_line("L55").position_after(position))
        position = 0
        self.assertEqual(99, Rotation.from_line("L1").position_after(position))
        position = 99
        self.assertEqual(0, Rotation.from_line("L99").position_after(position))
        position = 0
        self.assertEqual(14, Rotation.from_line("R14").position_after(position))
        position = 14
        self.assertEqual(32, Rotation.from_line("L82").position_after(position))
