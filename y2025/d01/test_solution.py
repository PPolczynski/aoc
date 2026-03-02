from unittest import TestCase

from y2025.d01.solution import Rotation


class TestRotation(TestCase):
    def test_from_line(self):
        self.assertEqual(Rotation(-1, 68, 0), Rotation.from_line("L68"))
        self.assertEqual(Rotation(1, 48, 0), Rotation.from_line("R48"))
        self.assertEqual(Rotation(-1, 1, 0), Rotation.from_line("L1"))
        self.assertEqual(Rotation(-1, 0, 1), Rotation.from_line("L100"))
        self.assertEqual(Rotation(1, 0, 1), Rotation.from_line("R100"))
        self.assertEqual(Rotation(-1, 1, 1), Rotation.from_line("L101"))
        self.assertEqual(Rotation(-1, 99, 1), Rotation.from_line("L199"))

    def test_position_after(self):
        self.assertEqual((82, True), Rotation.from_line("L68").rotate_from(50))
        self.assertEqual((52, False), Rotation.from_line("L30").rotate_from(82))
        self.assertEqual((0, True), Rotation.from_line("R48").rotate_from(52))
        self.assertEqual((95, True), Rotation.from_line("L5").rotate_from(0))
        self.assertEqual((55, True), Rotation.from_line("R60").rotate_from(95))
        self.assertEqual((0, False), Rotation.from_line("L55").rotate_from(55))
        self.assertEqual((99, True), Rotation.from_line("L1").rotate_from(0))
        self.assertEqual((0, False), Rotation.from_line("L99").rotate_from(99))
        self.assertEqual((14, False), Rotation.from_line("R14").rotate_from(0))
        self.assertEqual((32, True), Rotation.from_line("L82").rotate_from(14))

    def test_rotate_from_with_pass_cnt(self):
        self.assertEqual((82, 1), Rotation.from_line("L68").rotate_from_with_pass_cnt(50))
        self.assertEqual((52, 0), Rotation.from_line("L30").rotate_from_with_pass_cnt(82))
        self.assertEqual((0, 1), Rotation.from_line("R48").rotate_from_with_pass_cnt(52))
        self.assertEqual((95, 0), Rotation.from_line("L5").rotate_from_with_pass_cnt(0))
        self.assertEqual((55, 1), Rotation.from_line("R60").rotate_from_with_pass_cnt(95))
        self.assertEqual((0, 1), Rotation.from_line("L55").rotate_from_with_pass_cnt(55))
        self.assertEqual((99, 0), Rotation.from_line("L1").rotate_from_with_pass_cnt(0))
        self.assertEqual((0, 1), Rotation.from_line("L99").rotate_from_with_pass_cnt(99))
        self.assertEqual((14, 0), Rotation.from_line("R14").rotate_from_with_pass_cnt(0))
        self.assertEqual((32, 1), Rotation.from_line("L82").rotate_from_with_pass_cnt(14))
        # non example
        self.assertEqual((50, 10), Rotation.from_line("R1000").rotate_from_with_pass_cnt(50))
