from unittest import TestCase

from y2023.d24.solution import HailStone


class TestHailStone(TestCase):

    def test_intersects_xy(self):
        def check_intersection(s1: str, s2: str, want_intersection: bool,
                               want_coordinate: tuple[float, float] | None = None):
            h1 = HailStone.from_line(s1)
            h2 = HailStone.from_line(s2)
            intersects, cords = h1.intersects_xy(h2)
            self.assertEqual(intersects, want_intersection)
            if want_intersection:
                self.assertAlmostEqual(cords[0], want_coordinate[0], 3)
                self.assertAlmostEqual(cords[1], want_coordinate[1], 3)
            else:
                self.assertIsNone(cords)

        check_intersection("19, 13, 30 @ -2, 1, -2", "18, 19, 22 @ -1, -1, -2", want_intersection=True,
                           want_coordinate=(14.333, 15.333))
        check_intersection("19, 13, 30 @ -2, 1, -2", "20, 25, 34 @ -2, -2, -4", want_intersection=True,
                           want_coordinate=(11.667, 16.667))
        # intersect in past
        check_intersection("19, 13, 30 @ -2, 1, -2", "20, 19, 15 @ 1, -5, -3", want_intersection=False)
        # parallel
        check_intersection("18, 19, 22 @ -1, -1, -2", "20, 25, 34 @ -2, -2, -4", want_intersection=False)
