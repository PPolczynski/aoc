class Node:
    def __init__(self):
        self.next = set()
        self.prev = set()

class PrintQueue:
    def __init__(self, printer_configuration: list[str]):
        config = dict()
        for configuration in printer_configuration:
            first, second = [int(x) for x in configuration.split("|")]
            if first not in config:
                config[first] = Node()
                config[first].next.add(second)
            else:
                config[first].next.add(second)
            if second not in config:
                config[second] = Node()
                config[second].prev.add(first)
            else:
                config[second].prev.add(first)
        self._config = config

    def get_correctly_ordered_middle_sum(self, print_orders: list[str]) -> int:
        middle_value_sum = 0
        for print_order_str in print_orders:
            print_order = [int(num) for num in print_order_str.split(",")]
            if self._is_print_correctly_ordered(print_order):
                mid = len(print_order) // 2
                middle_value_sum += print_order[mid]
        return middle_value_sum

    def get_incorrectly_ordered_middle_sum(self, print_orders: list[str]) -> int:
        middle_value_sum = 0
        for print_order_str in print_orders:
            print_order = [int(num) for num in print_order_str.split(",")]
            if not self._is_print_correctly_ordered(print_order):
                print_order = self._get_correct_print_order(print_order)
                mid = len(print_order) // 2
                middle_value_sum += print_order[mid]
        return middle_value_sum

    def _is_print_correctly_ordered(self, print_order: list[int]) -> bool:
        prev = print_order[0]
        for page_number in print_order[1:]:
            if not self._can_be_followed_by_number(prev, page_number):
                return False
            prev = page_number
        return True

    def _get_correct_print_order(self, print_order: list[int]) -> list[int]:
        prev = print_order[0]
        for idx, page_number in enumerate(print_order[1:]):
            if not self._can_be_followed_by_number(prev, page_number):
                tmp = page_number
                print_order[idx + 1] = prev
                print_order[idx] = tmp
                return self._get_correct_print_order(print_order)
            prev = page_number
        return print_order

    def _can_be_followed_by_number(self, prev, current) -> bool:
        return prev == current or current in self._config.get(prev).next or prev in self._config.get(current).prev
