import unittest

from y2023.d12.hot_springs import HotSprings


class HotSpringsTestCase(unittest.TestCase):
    def test_get_arrangements_count(self):
        self.assertEqual(1, HotSprings.get_arrangements_count("???.### 1,1,3"))
        self.assertEqual(4, HotSprings.get_arrangements_count(".??..??...?##. 1,1,3"))
        self.assertEqual(1, HotSprings.get_arrangements_count("?#?#?#?#?#?#?#? 1,3,1,6"))
        self.assertEqual(1, HotSprings.get_arrangements_count("????.#...#... 4,1,1"))
        self.assertEqual(4, HotSprings.get_arrangements_count("????.######..#####. 1,6,5"))
        self.assertEqual(10, HotSprings.get_arrangements_count("?###???????? 3,2,1"))

    def test_get_arrangements_count_in_records(self):
        records = [
            "???.### 1,1,3",
            ".??..??...?##. 1,1,3",
            "?#?#?#?#?#?#?#? 1,3,1,6",
            "????.#...#... 4,1,1",
            "????.######..#####. 1,6,5",
            "?###???????? 3,2,1"
        ]
        self.assertEqual(21, HotSprings.get_arrangements_count_in_records(records))

    def test_get_arrangements_count_unfolded(self):
        records = [
            "???.### 1,1,3",
            ".??..??...?##. 1,1,3",
            "?#?#?#?#?#?#?#? 1,3,1,6",
            "????.#...#... 4,1,1",
            "????.######..#####. 1,6,5",
            "?###???????? 3,2,1"
        ]
        self.assertEqual(525152, HotSprings.get_arrangements_count_in_records_unfolded(records, 5))

if __name__ == '__main__':
    unittest.main()
