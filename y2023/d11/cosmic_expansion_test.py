import unittest

from y2023.d11.cosmic_expansion import CosmicExpansion


class CosmicExpansionTestCase(unittest.TestCase):
    def test_get_galaxy_distance_sum_2(self):
        galaxy = [
            "...#......",
            ".......#..",
            "#.........",
            "..........",
            "......#...",
            ".#........",
            ".........#",
            "..........",
            ".......#..",
            "#...#....."
            ]

        cosmic_expansion = CosmicExpansion(galaxy, 2)
        self.assertEqual(374, cosmic_expansion.get_galaxy_distance_sum())

    def test_get_galaxy_distance_sum_10(self):
        galaxy = [
            "...#......",
            ".......#..",
            "#.........",
            "..........",
            "......#...",
            ".#........",
            ".........#",
            "..........",
            ".......#..",
            "#...#....."
            ]

        cosmic_expansion = CosmicExpansion(galaxy, 10)
        self.assertEqual(1030, cosmic_expansion.get_galaxy_distance_sum())

    def test_get_galaxy_distance_sum_100(self):
        galaxy = [
            "...#......",
            ".......#..",
            "#.........",
            "..........",
            "......#...",
            ".#........",
            ".........#",
            "..........",
            ".......#..",
            "#...#....."
            ]

        cosmic_expansion = CosmicExpansion(galaxy, 100)
        self.assertEqual(8410, cosmic_expansion.get_galaxy_distance_sum())


if __name__ == '__main__':
    unittest.main()
