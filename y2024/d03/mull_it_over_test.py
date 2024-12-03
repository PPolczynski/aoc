import unittest

from y2024.d03.mull_it_over import MullItOver


class MullItOverCase(unittest.TestCase):
    def test_get_sum_of_multiplications(self):
        corrupted_memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        result = MullItOver.get_sum_of_multiplications(corrupted_memory)
        self.assertEqual(result, 161)

    def test_get_sum_of_multiplications_conditional(self):
        corrupted_memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        result = MullItOver.get_sum_of_multiplications_conditional(corrupted_memory)
        self.assertEqual(result, 48)

if __name__ == '__main__':
    unittest.main()
