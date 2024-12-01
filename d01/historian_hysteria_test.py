import unittest

from d01.historian_hysteria import HistorianHysteria


class MyTestCase(unittest.TestCase):
    def test_example_distance(self):
        list_a = [3, 4, 2, 1, 3, 3]
        list_b = [4, 3, 5, 3, 9, 3]
        historian_hysteria = HistorianHysteria(list_a, list_b)
        distance = historian_hysteria.get_list_distance()
        self.assertEqual(distance, 11)

    def test_example_similarity(self):
        list_a = [3, 4, 2, 1, 3, 3]
        list_b = [4, 3, 5, 3, 9, 3]
        historian_hysteria = HistorianHysteria(list_a, list_b)
        similarity = historian_hysteria.get_list_similarity()
        self.assertEqual(similarity, 31)


if __name__ == '__main__':
    unittest.main()
