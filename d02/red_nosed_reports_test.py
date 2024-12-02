import unittest

from d02.red_nosed_reports import RedNosedReports


class RedNosedReportsTestCase(unittest.TestCase):
    def test_get_safe_levels_count(self):
        reports = [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9]
        ]
        red_nosed_reports = RedNosedReports(reports)
        number_of_safe_reports = red_nosed_reports.get_safe_levels_count()
        self.assertEqual(number_of_safe_reports, 2)


if __name__ == '__main__':
    unittest.main()