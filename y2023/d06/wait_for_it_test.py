import unittest

from y2023.d06.wait_for_It import WaitForIt


class WaitForItTestCase(unittest.TestCase):
    def test_get_distance(self):
        self.assertEqual(0, WaitForIt.get_distance(7, 0))
        self.assertEqual(6, WaitForIt.get_distance(7, 1))
        self.assertEqual(10, WaitForIt.get_distance(7, 2))
        self.assertEqual(12, WaitForIt.get_distance(7, 3))
        self.assertEqual(12, WaitForIt.get_distance(7, 4))
        self.assertEqual(10, WaitForIt.get_distance(7, 5))
        self.assertEqual(6, WaitForIt.get_distance(7, 6))
        self.assertEqual(0, WaitForIt.get_distance(7, 7))

    def test_ways_to_beat_time(self):
        self.assertEqual(4, WaitForIt.ways_to_beat_time(7, 9))
        self.assertEqual(8, WaitForIt.ways_to_beat_time(15, 40))
        self.assertEqual(9, WaitForIt.ways_to_beat_time(30, 200))

    def test_get_product_ways_to_beat_time(self):
        races = [
            (7, 9),
            (15, 40),
            (30, 200)
        ]
        self.assertEqual(288, WaitForIt.get_product_ways_to_beat_time(races))

if __name__ == '__main__':
    unittest.main()
