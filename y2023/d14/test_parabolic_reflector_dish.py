from unittest import TestCase

from y2023.d14.parabolic_reflector_dish import ParabolicReflectorDish


class TestParabolicReflectorDish(TestCase):
    def test_get_total_load_north(self):
        platform = [
            "O....#....",
            "O.OO#....#",
            ".....##...",
            "OO.#O....O",
            ".O.....O#.",
            "O.#..O.#.#",
            "..O..#O..O",
            ".......O..",
            "#....###..",
            "#OO..#...."
        ]
        parabolic_reflector_dish = ParabolicReflectorDish(platform)
        parabolic_reflector_dish.tilt_north()
        self.assertEqual(136, parabolic_reflector_dish.get_total_load_north_beams())
