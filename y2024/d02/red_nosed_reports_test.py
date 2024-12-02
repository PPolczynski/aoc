import unittest

from y2024.d02.red_nosed_reports import RedNosedReports

_example_reports = [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9]
        ]

class RedNosedReportsTestCase(unittest.TestCase):
    def test_example_get_safe_reports_count(self):
        red_nosed_reports = RedNosedReports(_example_reports)
        number_of_safe_reports = red_nosed_reports.get_safe_reports_count()
        self.assertEqual(number_of_safe_reports, 2)

    def test_example_get_safe_reports_count_with_tolerance(self):
        red_nosed_reports = RedNosedReports(_example_reports)
        number_of_safe_reports = red_nosed_reports.get_safe_reports_count_with_tolerance()
        self.assertEqual(number_of_safe_reports, 4)

    def test_own_get_safe_reports_count(self):
        reports = [
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 0, 3, 4, 5, 6, 7, 8],
            [2, 2, 3, 4, 5, 6, 7, 8],
            [3, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 3, 5, 6, 7, 8],
            [1, 2, 3, 2, 5, 6, 7, 8]
        ]
        red_nosed_reports = RedNosedReports(reports)
        number_of_safe_reports = red_nosed_reports.get_safe_reports_count_with_tolerance()
        self.assertEqual(number_of_safe_reports, len(reports))

if __name__ == '__main__':
    unittest.main()