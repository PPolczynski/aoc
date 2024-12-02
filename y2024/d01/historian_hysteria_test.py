import unittest

from y2024.d01.historian_hysteria import HistorianHysteria

_list_a = [3, 4, 2, 1, 3, 3]
_list_b = [4, 3, 5, 3, 9, 3]

class HistorianHysteriaTestCase(unittest.TestCase):
    def test_example_distance(self):
        historian_hysteria = HistorianHysteria(_list_a, _list_b)
        distance = historian_hysteria.get_list_distance()
        self.assertEqual(distance, 11)

    def test_example_similarity(self):
        historian_hysteria = HistorianHysteria(_list_a, _list_b)
        similarity = historian_hysteria.get_list_similarity()
        self.assertEqual(similarity, 31)


if __name__ == '__main__':
    unittest.main()
