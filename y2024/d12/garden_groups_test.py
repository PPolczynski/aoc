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

    def test_get_fencing_cost_bulk_example1(self):
        garden = [
            "AAAA",
            "BBCD",
            "BBCC",
            "EEEC"
        ]
        garden_groups = GardenGroups(garden)
        self.assertEqual(80, garden_groups.get_fencing_cost_bulk())

    def test_get_fencing_cost_bulk_example2(self):
        garden = [
            "OOOOO",
            "OXOXO",
            "OOOOO",
            "OXOXO",
            "OOOOO"
        ]
        garden_groups = GardenGroups(garden)
        self.assertEqual(436, garden_groups.get_fencing_cost_bulk())

    def test_get_fencing_cost_bulk_example3(self):
        garden = [
            "EEEEE",
            "EXXXX",
            "EEEEE",
            "EXXXX",
            "EEEEE"
        ]
        garden_groups = GardenGroups(garden)
        self.assertEqual(236, garden_groups.get_fencing_cost_bulk())

    def test_get_fencing_cost_bulk_example4(self):
        garden = [
            "AAAAAA",
            "AAABBA",
            "AAABBA",
            "ABBAAA",
            "ABBAAA",
            "AAAAAA"
        ]
        garden_groups = GardenGroups(garden)
        self.assertEqual(368, garden_groups.get_fencing_cost_bulk())

    def test_get_fencing_cost_bulk_example5(self):
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
        self.assertEqual(1206, garden_groups.get_fencing_cost_bulk())

    def test_get_fencing_cost_bulk_example6(self):
        garden = [
            "AAAEAAAAAA",
            "FFAEAADAAA",
            "FFAAAADACA",
            "FFAABAAAAB",
            "FFABBBABBB",
            "FAAAABBBBB",
            "FAGGABBBBB",
            "FAGAABBBBB"
        ]
        garden_groups = GardenGroups(garden)
        self.assertEqual(1992, garden_groups.get_fencing_cost_bulk())

    def test_get_fencing_cost_bulk_example7(self):
        garden = [
            "LDDDDDDXXX",
            "LLLDDVDXXX",
            "LLLDDDXXXX"
        ]
        garden_groups = GardenGroups(garden)
        self.assertEqual(250, garden_groups.get_fencing_cost_bulk())

    def test_get_fencing_cost_bulk_example8(self):
        garden = [
            "BBBBBC",
            "BAAABC",
            "BABABC",
            "BAABBB",
            "BABABC",
            "BAAABC"
        ]
        garden_groups = GardenGroups(garden)
        self.assertEqual(492, garden_groups.get_fencing_cost_bulk())

    def test_get_fencing_cost_bulk_example9(self):
        garden = [
            "AAAAA",
            "ABABA",
            "ABBBA",
            "ABABA"
        ]
        garden_groups = GardenGroups(garden)
        self.assertEqual(232, garden_groups.get_fencing_cost_bulk())

    def test_get_fencing_cost_bulk_example10(self):
        garden = [
            "----",
            "-OOO",
            "-O-O",
            "OO-O",
            "-OOO"
        ]
        garden_groups = GardenGroups(garden)
        self.assertEqual(180, garden_groups.get_fencing_cost_bulk())


    def test_get_fencing_cost_bulk_example11(self):
        garden = [
            "----",
            "OOO-",
            "O-O-",
            "O-OO",
            "OOO-"
        ]
        garden_groups = GardenGroups(garden)
        self.assertEqual(180, garden_groups.get_fencing_cost_bulk())

if __name__ == '__main__':
    unittest.main()
