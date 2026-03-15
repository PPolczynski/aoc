from unittest import TestCase

from y2025.d10.solution import Machine


class TestMachine(TestCase):
    def test_from_line(self):
        self.assertEqual(Machine.from_line("[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"),
                         Machine(
                             6,
                             [1, 5, 2, 3, 10, 12],
                             [3, 5, 4, 7]))
        self.assertEqual(Machine.from_line("[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}"),
                         Machine(
                             2,
                             [23, 6, 17, 28, 15],
                             [7, 5, 12, 7, 2]))
        self.assertEqual(Machine.from_line("[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"),
                         Machine(
                             29,
                             [62, 38, 59, 24], [10, 11, 11, 5, 10, 5]))

    def test_min_presses(self):
        m1 = Machine.from_line("[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}")
        self.assertEqual(m1.target, m1.buttons[0] ^ m1.buttons[1] ^ m1.buttons[2])
        self.assertEqual(m1.target, m1.buttons[1] ^ m1.buttons[3] ^ m1.buttons[5] ^ m1.buttons[5])
        self.assertEqual(m1.target, m1.buttons[1] ^ m1.buttons[3])
        self.assertEqual(m1.target, m1.buttons[0] ^ m1.buttons[2] ^ m1.buttons[3] ^ m1.buttons[4] ^ m1.buttons[5])
        self.assertEqual(m1.min_presses(), 2)
        m2 = Machine.from_line("[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}")
        self.assertEqual(m2.target, m2.buttons[2] ^ m2.buttons[3] ^ m2.buttons[4])
        self.assertEqual(m2.min_presses(), 3)
        m3 = Machine.from_line("[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}")
        self.assertEqual(m3.target, m3.buttons[1] ^ m3.buttons[2])
        self.assertEqual(m3.min_presses(), 2)
