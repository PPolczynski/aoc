import unittest

from y2024.d10.hoof_it import HoofIt


class HoofItTestCase(unittest.TestCase):
    def test_get_trailheads_score_sum(self):
        topographic_map = [
            "0123",
            "1234",
            "8765",
            "9876"
        ]
        hoof_it = HoofIt(topographic_map)
        self.assertEqual(1, hoof_it.get_trailheads_score_sum())

    def test_get_trailheads_score_sum2(self):
        topographic_map = [
            "...0...",
            "...1...",
            "...2...",
            "6543456",
            "7.....7",
            "8.....8",
            "9.....9"
        ]
        hoof_it = HoofIt(topographic_map)
        self.assertEqual(2, hoof_it.get_trailheads_score_sum())

    def test_get_trailheads_score_sum3(self):
        topographic_map = [
            "..90..9",
            "...1.98",
            "...2..7",
            "6543456",
            "765.987",
            "876....",
            "987...."
        ]
        hoof_it = HoofIt(topographic_map)
        self.assertEqual(4, hoof_it.get_trailheads_score_sum())

    def test_get_trailheads_score_sum4(self):
        topographic_map = [
            "89010123",
            "78121874",
            "87430965",
            "96549874",
            "45678903",
            "32019012",
            "01329801",
            "10456732"
        ]
        hoof_it = HoofIt(topographic_map)
        self.assertEqual(36, hoof_it.get_trailheads_score_sum())

    def test_get_trailheads_score_distinct_paths_sum(self):
        topographic_map = [
            ".....0.",
            "..4321.",
            "..5..2.",
            "..6543.",
            "..7..4.",
            "..8765.",
            "..9...."
        ]
        hoof_it = HoofIt(topographic_map)
        self.assertEqual(3, hoof_it.get_trailheads_score_distinct_paths_sum())

    def test_get_trailheads_score_distinct_paths_sum2(self):
        topographic_map = [
            "..90..9",
            "...1.98",
            "...2..7",
            "6543456",
            "765.987",
            "876....",
            "987...."
        ]
        hoof_it = HoofIt(topographic_map)
        self.assertEqual(13, hoof_it.get_trailheads_score_distinct_paths_sum())

    def test_get_trailheads_score_distinct_paths_sum3(self):
        topographic_map = [
            "012345",
            "123456",
            "234567",
            "345678",
            "4.6789",
            "56789."
        ]
        hoof_it = HoofIt(topographic_map)
        self.assertEqual(227, hoof_it.get_trailheads_score_distinct_paths_sum())

    def test_get_trailheads_score_distinct_paths_sum4(self):
        topographic_map = [
            "89010123",
            "78121874",
            "87430965",
            "96549874",
            "45678903",
            "32019012",
            "01329801",
            "10456732"
        ]
        hoof_it = HoofIt(topographic_map)
        self.assertEqual(81, hoof_it.get_trailheads_score_distinct_paths_sum())

if __name__ == '__main__':
    unittest.main()
