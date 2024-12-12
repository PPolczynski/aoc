from y2024.d12.garden_groups import GardenGroups
import unittest


class MyTestCase(unittest.TestCase):\

    def test_get_fencing_cost_example1(self):
        garden = [
            "AAAA",
            "BBCD",
            "BBCC",
            "EEEC"
        ]
        garden_groups = GardenGroups(garden)
        self.assertEqual(140, garden_groups.get_fencing_cost())

    def test_get_fencing_cost_example2(self):
        garden = [
            "OOOOO",
            "OXOXO",
            "OOOOO",
            "OXOXO",
            "OOOOO"
        ]
        garden_groups = GardenGroups(garden)
        self.assertEqual(772, garden_groups.get_fencing_cost())

    def test_get_fencing_cost_example3(self):
        garden = [
            "RRRRIICCFF",
            "RRRRIICCCF",
            "VVRRRCCFFF",
            "VVRCCCJFFF",
            "VVVVCJJCFE",
            "VVIVCCJJEE",
            "VVIIICJJEE",
            "MIIIIIJJEE",
            "MIIISIJEEE",
            "MMMISSJEEE"
        ]
        garden_groups = GardenGroups(garden)
        self.assertEqual(1930, garden_groups.get_fencing_cost())


if __name__ == '__main__':
    unittest.main()
