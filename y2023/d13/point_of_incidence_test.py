import unittest

from y2023.d13.point_of_incidence import PointOfIncidence


class PointOfIncidenceTestCase(unittest.TestCase):
    def test_get_reflection(self):
        lava_map = [
            "#.##..##.",
            "..#.##.#.",
            "##......#",
            "##......#",
            "..#.##.#.",
            "..##..##.",
            "#.#.##.#."
        ]
        self.assertEqual(5, PointOfIncidence.get_reflection(lava_map))

    def test_get_reflection2(self):
        lava_map = [
            "#...##..#",
            "#....#..#",
            "..##..###",
            "#####.##.",
            "#####.##.",
            "..##..###",
            "#....#..#"
        ]
        self.assertEqual(400, PointOfIncidence.get_reflection(lava_map))

    def test_get_reflection_sum(self):
        lava_map = [
            [
            "#.##..##.",
            "..#.##.#.",
            "##......#",
            "##......#",
            "..#.##.#.",
            "..##..##.",
            "#.#.##.#."
            ],
            [
            "#...##..#",
            "#....#..#",
            "..##..###",
            "#####.##.",
            "#####.##.",
            "..##..###",
            "#....#..#"
        ]]
        self.assertEqual(405, PointOfIncidence.get_reflection_sum(lava_map))

    def test_get_reflection_sum_of_by(self):
        lava_map = [
            [
            "#.##..##.",
            "..#.##.#.",
            "##......#",
            "##......#",
            "..#.##.#.",
            "..##..##.",
            "#.#.##.#."
            ],
            [
            "#...##..#",
            "#....#..#",
            "..##..###",
            "#####.##.",
            "#####.##.",
            "..##..###",
            "#....#..#"
        ]]
        self.assertEqual(400, PointOfIncidence.get_reflection_sum_of_by(lava_map, 1))

if __name__ == '__main__':
    unittest.main()
