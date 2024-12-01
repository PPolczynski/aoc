import unittest

from d01.historian_hysteria import HistorianHysteria


class MyTestCase(unittest.TestCase):
    def test_example_distance(self):
        l1 = [3, 4, 2, 1, 3, 3]
        l2 = [4, 3, 5, 3, 9, 3]
        hysteria = HistorianHysteria(l1, l2)
        distance = hysteria.get_list_distance()
        self.assertEqual(distance, 11)  # add assertion here

    def test_example_similarity(self):
        l1 = [3, 4, 2, 1, 3, 3]
        l2 = [4, 3, 5, 3, 9, 3]
        hysteria = HistorianHysteria(l1, l2)
        similarity = hysteria.get_list_similarity()
        self.assertEqual(similarity, 31)  # add assertion here


if __name__ == '__main__':
    unittest.main()
