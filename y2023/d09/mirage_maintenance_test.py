import unittest

from y2023.d09.mirage_maintenance import Report, MirageMaintenance


class MirageMaintenanceTestCase(unittest.TestCase):
    def test_report(self):
        report = Report([0, 3, 6, 9, 12, 15])
        self.assertEqual(18, report.get_next_value())
        report1 = Report([1, 3, 6, 10, 15, 21])
        self.assertEqual(28, report1.get_next_value())
        report2 = Report([10, 13, 16, 21, 30, 45])
        self.assertEqual(68, report2.get_next_value())
        report2 = Report([10, 13, 16, 21, 30, 45])
        self.assertEqual(5, report2.get_previous_value())

    def test_get_extrapolated_values_sum(self):
        lines = [
            "0 3 6 9 12 15",
            "1 3 6 10 15 21",
            "10 13 16 21 30 45"
        ]
        mirage_maintenance = MirageMaintenance(lines)
        self.assertEqual(114, mirage_maintenance.get_extrapolated_values_sum())
        self.assertEqual(2, mirage_maintenance.get_extrapolated_previous_values_sum())

if __name__ == '__main__':
    unittest.main()
