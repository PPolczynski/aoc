import unittest

from y2024.d04.ceres_cearch import CeresSearch


class CeresSearchTestCase(unittest.TestCase):
    def test_get_occurrence_count_example_1(self):
        puzzle = [
            "..X...",
            ".SAMX.",
            ".A..A.",
            "XMAS.S",
            ".X...."
            ]
        ceres_search = CeresSearch(puzzle)
        self.assertEqual(ceres_search.get_occurrence_count("XMAS"), 4)

    def test_get_occurrence_count_example_2(self):
        puzzle = [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX"
            ]
        ceres_search = CeresSearch(puzzle)
        self.assertEqual(ceres_search.get_occurrence_count("XMAS"), 18)

    def test_get_x_mas_occurrence_count_example_1(self):
        puzzle = [
            "M.S",
            ".A.",
            "M.S"
            ]
        ceres_search = CeresSearch(puzzle)
        self.assertEqual(ceres_search.get_x_mas_occurrence_count(), 1)

    def test_get_x_mas_occurrence_count_example_2(self):
        puzzle = [
            ".M.S......",
            "..A..MSMS.",
            ".M.S.MAA..",
            "..A.ASMSM.",
            ".M.S.M....",
            "..........",
            "S.S.S.S.S.",
            ".A.A.A.A..",
            "M.M.M.M.M.",
            ".........."
        ]
        ceres_search = CeresSearch(puzzle)
        self.assertEqual(ceres_search.get_x_mas_occurrence_count(), 9)

if __name__ == '__main__':
    unittest.main()
