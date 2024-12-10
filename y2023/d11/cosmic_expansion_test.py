import unittest

from y2023.d11.cosmic_expansion import CosmicExpansion


class CosmicExpansionTestCase(unittest.TestCase):
    def test_something(self):
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

        cosmic_expansion = CosmicExpansion(galaxy)
        self.assertEqual(374, cosmic_expansion.get_galaxy_distance_sum())


if __name__ == '__main__':
    unittest.main()
