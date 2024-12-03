import unittest

from y2023.d03.gear_ratios import GearRatios


class GearRatiosTestCase(unittest.TestCase):
    def test_get_sum_part_numbers(self):
        schematics = ["467..114..",
                        "...*......",
                        "..35..633.",
                        "......#...",
                        "617*......",
                        ".....+.58.",
                        "..592.....",
                        "......755.",
                        "...$.*....",
                        ".664.598.."]
        gear_ratios = GearRatios(schematics)

        self.assertEqual(gear_ratios.get_sum_part_numbers(), 4361)

    def test_get_sum_gear_ratio(self):
        schematics = ["467..114..",
                        "...*......",
                        "..35..633.",
                        "......#...",
                        "617*......",
                        ".....+.58.",
                        "..592.....",
                        "......755.",
                        "...$.*....",
                        ".664.598.."]
        gear_ratios = GearRatios(schematics)

        self.assertEqual(gear_ratios.get_sum_gear_ratio(), 467835)

if __name__ == '__main__':
    unittest.main()
