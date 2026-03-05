from unittest import TestCase

from y2025.d02.solution import ProductRange


class TestProductRange(TestCase):
    def test_get_ids_within(self):
        self.assertListEqual([11, 22], ProductRange.from_string("11-22").get_invalid_ids())
        self.assertListEqual([99], ProductRange.from_string("95-115").get_invalid_ids())
        self.assertListEqual([1010], ProductRange.from_string("998-1012").get_invalid_ids())
        self.assertListEqual([1188511885], ProductRange.from_string("1188511880-1188511890").get_invalid_ids())
        self.assertListEqual([222222], ProductRange.from_string("222220-222224").get_invalid_ids())
        self.assertListEqual([], ProductRange.from_string("1698522-1698528").get_invalid_ids())
        self.assertListEqual([446446], ProductRange.from_string("446443-446449").get_invalid_ids())
        self.assertListEqual([38593859], ProductRange.from_string("38593856-38593862").get_invalid_ids())
        self.assertListEqual([11], ProductRange.from_string("11-11").get_invalid_ids())
        self.assertListEqual([], ProductRange.from_string("1-1").get_invalid_ids())
        self.assertListEqual([22, 33], ProductRange.from_string("16-33").get_invalid_ids())

    def test_get_all_ids_within(self):
        def lists_equal_without_order(want, got):
            self.assertListEqual(sorted(want), sorted(got))

        lists_equal_without_order([11, 22], ProductRange.from_string("11-22").get_all_invalid_ids())
        lists_equal_without_order([99, 111], ProductRange.from_string("95-115").get_all_invalid_ids())
        lists_equal_without_order([999, 1010], ProductRange.from_string("998-1012").get_all_invalid_ids())
        lists_equal_without_order([1188511885], ProductRange.from_string("1188511880-1188511890").get_all_invalid_ids())
        lists_equal_without_order([222222], ProductRange.from_string("222220-222224").get_all_invalid_ids())
        lists_equal_without_order([], ProductRange.from_string("1698522-1698528").get_all_invalid_ids())
        lists_equal_without_order([446446], ProductRange.from_string("446443-446449").get_all_invalid_ids())
        lists_equal_without_order([38593859], ProductRange.from_string("38593856-38593862").get_all_invalid_ids())
        lists_equal_without_order([565656], ProductRange.from_string("565653-565659").get_all_invalid_ids())
        lists_equal_without_order([824824824], ProductRange.from_string("824824821-824824827").get_all_invalid_ids())
        lists_equal_without_order([2121212121], ProductRange.from_string("2121212118-2121212124").get_all_invalid_ids())
        lists_equal_without_order([11], ProductRange.from_string("11-11").get_all_invalid_ids())
        lists_equal_without_order([], ProductRange.from_string("1-1").get_all_invalid_ids())
        lists_equal_without_order([22, 33], ProductRange.from_string("16-33").get_all_invalid_ids())
        lists_equal_without_order([11, 22, 33], ProductRange.from_string("1-33").get_all_invalid_ids())
