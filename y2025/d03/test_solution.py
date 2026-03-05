from unittest import TestCase

from y2025.d03.solution import max_subsequence_value, max_subsequence_of_length_value


def str_to_list_int(s: str) -> list[int]:
    return [int(c) for c in s[:]]


class Test(TestCase):
    def test_max_subsequence_value(self):
        self.assertEqual(98, max_subsequence_value(str_to_list_int("987654321111111")))
        self.assertEqual(89, max_subsequence_value(str_to_list_int("811111111111119")))
        self.assertEqual(78, max_subsequence_value(str_to_list_int("234234234234278")))
        self.assertEqual(92, max_subsequence_value(str_to_list_int("818181911112111")))
        self.assertEqual(22, max_subsequence_value(str_to_list_int("22")))

    def test_max_subsequence_of_length_value(self):
        # 2
        self.assertEqual(98, max_subsequence_of_length_value(str_to_list_int("987654321111111"), 2))
        self.assertEqual(89, max_subsequence_of_length_value(str_to_list_int("811111111111119"), 2))
        self.assertEqual(78, max_subsequence_of_length_value(str_to_list_int("234234234234278"), 2))
        self.assertEqual(92, max_subsequence_of_length_value(str_to_list_int("818181911112111"), 2))
        self.assertEqual(22, max_subsequence_of_length_value(str_to_list_int("22"), 2))
        # 12
        self.assertEqual(987654321111, max_subsequence_of_length_value(str_to_list_int("987654321111111"), 12))
        self.assertEqual(811111111119, max_subsequence_of_length_value(str_to_list_int("811111111111119"), 12))
        self.assertEqual(434234234278, max_subsequence_of_length_value(str_to_list_int("234234234234278"), 12))
        self.assertEqual(888911112111, max_subsequence_of_length_value(str_to_list_int("818181911112111"), 12))
