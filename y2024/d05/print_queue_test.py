import unittest

from y2024.d05.print_queue import PrintQueue

printer_input = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",
    "",
    "75,47,61,53,29",
    "97,61,53,29,13",
    "75,29,13",
    "75,97,47,61,53",
    "61,13,29",
    "97,13,75,29,47"
]

class PrintQueueTestCase(unittest.TestCase):
    def test_get_correctly_ordered_middle_sum(self):
        print_queue = PrintQueue(printer_input[:21])
        self.assertEqual(print_queue.get_correctly_ordered_middle_sum(printer_input[22:]), 143)

    def test_get_incorrectly_ordered_middle_sum(self):
        print_queue = PrintQueue(printer_input[:21])
        self.assertEqual(print_queue.get_incorrectly_ordered_middle_sum(printer_input[22:]), 123)

if __name__ == '__main__':
    unittest.main()
