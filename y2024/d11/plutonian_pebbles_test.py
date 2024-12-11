import unittest

from y2024.d11.plutonian_pebbles import PlutonianPebbles


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(2, PlutonianPebbles.count_stones("125 17", 0))
        self.assertEqual(3, PlutonianPebbles.count_stones("125 17", 1))
        self.assertEqual(4, PlutonianPebbles.count_stones("125 17", 2))
        self.assertEqual(5, PlutonianPebbles.count_stones("125 17", 3))
        self.assertEqual(9, PlutonianPebbles.count_stones("125 17", 4))
        self.assertEqual(13, PlutonianPebbles.count_stones("125 17", 5))
        self.assertEqual(22, PlutonianPebbles.count_stones("125 17", 6))
        self.assertEqual(55312, PlutonianPebbles.count_stones("125 17", 25))


if __name__ == '__main__':
    unittest.main()
