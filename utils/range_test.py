import unittest
from .range import Range, simplify_ranges


class RangeTestCase(unittest.TestCase):
    def test_range_contains(self):
        tests = [
            ("full overlap", Range(1, 5), Range(2, 4), True),
            ("disjoint", Range(1, 5), Range(6, 8), False),
            ("right overlap", Range(3, 5), Range(2, 4), False),
            ("left overlap", Range(3, 5), Range(4, 6), False),
            ("shared left edge", Range(3, 5), Range(5, 6), False),
            ("shared right edge", Range(3, 5), Range(2, 3), False),
            ("same", Range(3, 5), Range(3, 5), True),
        ]
        for name, r, other, want in tests:
            with self.subTest(name=name):
                self.assertEqual(r.contains(other), want)

    def test_range_is_contained(self):
        tests = [
            ("full overlap", Range(2, 4), Range(1, 5), True),
            ("disjoint", Range(6, 8), Range(1, 5), False),
            ("right overlap", Range(2, 4), Range(3, 5), False),
            ("left overlap", Range(4, 6), Range(3, 5), False),
            ("shared left edge", Range(5, 6), Range(3, 5), False),
            ("shared right edge", Range(2, 3), Range(3, 5), False),
            ("same", Range(3, 5), Range(3, 5), True),
        ]
        for name, r, other, want in tests:
            with self.subTest(name=name):
                self.assertEqual(r.is_contained_by(other), want)

    def test_range_overlaps(self):
        tests = [
            ("full overlap", Range(1, 5), Range(2, 4), True),
            ("disjoint", Range(1, 5), Range(6, 8), False),
            ("right overlap", Range(3, 5), Range(2, 4), True),
            ("left overlap", Range(3, 5), Range(4, 6), True),
            ("shared left edge", Range(3, 5), Range(5, 6), True),
            ("shared right edge", Range(3, 5), Range(2, 3), True),
            ("same", Range(3, 5), Range(3, 5), True),
            ("other contains this", Range(2, 4), Range(1, 5), True),
            ("this contains other", Range(1, 5), Range(2, 4), True),
        ]
        for name, r, other, want in tests:
            with self.subTest(name=name):
                self.assertEqual(r.overlaps(other), want)

    def test_range_len(self):
        tests = [
            ("positive", Range(1, 3), 3),
            ("negative", Range(-3, -1), 3),
            ("mixed", Range(-3, 3), 7),
            ("positive single", Range(3, 3), 1),
            ("zero single", Range(0, 0), 1),
            ("negative single", Range(-3, -3), 1),
        ]
        for name, r, want in tests:
            with self.subTest(name=name):
                self.assertEqual(len(r), want)

    def test_range_contains_value(self):
        tests = [
            ("inside", Range(1, 5), 3, True),
            ("left edge", Range(1, 5), 1, True),
            ("right edge", Range(1, 5), 5, True),
            ("outside left", Range(1, 5), 0, False),
            ("outside right", Range(1, 5), 6, False),
            ("negative inside", Range(-5, -1), -3, True),
        ]
        for name, r, val, want in tests:
            with self.subTest(name=name):
                self.assertEqual(r.contains_value(val), want)

    def test_range_merge(self):
        tests = [
            ("full overlap", Range(1, 5), Range(2, 4), Range(1, 5), False),
            ("disjoint", Range(1, 5), Range(6, 8), None, True),
            ("right overlap", Range(3, 5), Range(2, 4), Range(2, 5), False),
            ("left overlap", Range(3, 5), Range(4, 6), Range(3, 6), False),
            ("shared edge", Range(3, 5), Range(5, 6), Range(3, 6), False),
            ("same", Range(3, 5), Range(3, 5), Range(3, 5), False),
            ("this contains other", Range(1, 10), Range(2, 5), Range(1, 10), False),
            ("other contains this", Range(2, 5), Range(1, 10), Range(1, 10), False),
        ]
        for name, r, other, want, want_err in tests:
            with self.subTest(name=name):
                if want_err:
                    with self.assertRaises(ValueError):
                        r.merge(other)
                else:
                    self.assertEqual(r.merge(other), want)

    def test_simplify_ranges(self):
        tests = [
            (
                "overlapping and out of order",
                [Range(10, 20), Range(1, 5), Range(15, 25), Range(4, 7)],
                [Range(1, 7), Range(10, 25)],
            ),
            (
                "disjoint",
                [Range(1, 2), Range(4, 5), Range(7, 8)],
                [Range(1, 2), Range(4, 5), Range(7, 8)],
            ),
            (
                "nested",
                [Range(1, 10), Range(2, 5), Range(6, 9)],
                [Range(1, 10)],
            ),
            (
                "touching edges",
                [Range(1, 5), Range(5, 10)],
                [Range(1, 10)],
            ),
            ("empty", [], []),
            ("single", [Range(1, 1)], [Range(1, 1)]),
        ]
        for name, ranges, want in tests:
            with self.subTest(name=name):
                self.assertEqual(simplify_ranges(ranges), want)


if __name__ == '__main__':
    unittest.main()
