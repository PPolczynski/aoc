from unittest import TestCase

from y2025.d09.solution import area


class Test(TestCase):
    def test_area(self):
        self.assertEqual(area((2, 5), (11, 1)), 50)
        self.assertEqual(area((2, 5), (9, 7)), 24)
        self.assertEqual(area((7, 1), (11, 7)), 35)
        self.assertEqual(area((7, 3), (2, 3)), 6)
