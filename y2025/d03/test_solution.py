from unittest import TestCase

from y2025.d03.solution import max_subsequence_value


class Test(TestCase):
    def test_max_subsequence_value(self):
        def str_to_list_int(s: str) -> list[int]:
            return [int(c) for c in s[:]]

        self.assertEqual(98, max_subsequence_value(str_to_list_int("987654321111111")))
        self.assertEqual(89, max_subsequence_value(str_to_list_int("811111111111119")))
        self.assertEqual(78, max_subsequence_value(str_to_list_int("234234234234278")))
        self.assertEqual(92, max_subsequence_value(str_to_list_int("818181911112111")))
        self.assertEqual(22, max_subsequence_value(str_to_list_int("22")))
