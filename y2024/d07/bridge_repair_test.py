import unittest

from y2024.d07.bridge_repair import BridgeRepair


class BridgeRepairTestCase(unittest.TestCase):
    def test_is_valid_something(self):
        self.assertEqual(True, BridgeRepair.is_valid(190, [10, 19]))
        self.assertEqual(True, BridgeRepair.is_valid(3267, [81, 40, 27]))
        self.assertEqual(False, BridgeRepair.is_valid(83, [17, 5]))
        self.assertEqual(False, BridgeRepair.is_valid(156, [15, 6]))
        self.assertEqual(False, BridgeRepair.is_valid(7290, [6, 8, 6, 15]))
        self.assertEqual(False, BridgeRepair.is_valid(161011, [16, 10, 13]))
        self.assertEqual(False, BridgeRepair.is_valid(192, [17, 8, 14]))
        self.assertEqual(False, BridgeRepair.is_valid(21037, [9, 7, 18, 13]))
        self.assertEqual(True, BridgeRepair.is_valid(292, [11, 6, 16, 20]))

    def test_is_valid_with_concat_something(self):
        self.assertEqual(True, BridgeRepair.is_valid_with_concat(190, [10, 19]))
        self.assertEqual(True, BridgeRepair.is_valid_with_concat(3267, [81, 40, 27]))
        self.assertEqual(False, BridgeRepair.is_valid_with_concat(83, [17, 5]))
        self.assertEqual(True, BridgeRepair.is_valid_with_concat(156, [15, 6]))
        self.assertEqual(True, BridgeRepair.is_valid_with_concat(7290, [6, 8, 6, 15]))
        self.assertEqual(False, BridgeRepair.is_valid_with_concat(161011, [16, 10, 13]))
        self.assertEqual(True, BridgeRepair.is_valid_with_concat(192, [17, 8, 14]))
        self.assertEqual(False, BridgeRepair.is_valid_with_concat(21037, [9, 7, 18, 13]))
        self.assertEqual(True, BridgeRepair.is_valid_with_concat(292, [11, 6, 16, 20]))

    def test_get_sum_valid_targets(self):
        total = BridgeRepair.get_sum_valid_targets([(190, [10, 19]), (3267, [81, 40, 27]), (83, [17, 5]),
                                                    (156, [15, 6]), (7290, [6, 8, 6, 15]), (161011, [16, 10, 13]),
                                                    (192, [17, 8, 14]), (21037, [9, 7, 18, 13]),
                                                    (292, [11, 6, 16, 20])])
        self.assertEqual(3749, total)

    def test_get_sum_valid_targets_with_concat(self):
        total = BridgeRepair.get_sum_valid_targets_with_concat([(190, [10, 19]), (3267, [81, 40, 27]), (83, [17, 5]),
                                                    (156, [15, 6]), (7290, [6, 8, 6, 15]), (161011, [16, 10, 13]),
                                                    (192, [17, 8, 14]), (21037, [9, 7, 18, 13]),
                                                    (292, [11, 6, 16, 20])])
        self.assertEqual(11387, total)

if __name__ == '__main__':
    unittest.main()
