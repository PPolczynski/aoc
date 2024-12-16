import time

from y2024.d05.solution import Printer

if __name__ == '__main__':
    rules = []
    print_orders = []
    is_rules = True
    with open("data", "r") as data_file:
        for line in data_file:
            if line.rstrip() == "":
                is_rules = False
            elif is_rules:
                rules.append(line.rstrip())
            else:
                print_orders.append(line.rstrip())

    print_queue = Printer(rules)
    print("Part 1:")
    start = time.time()
    print(f"{print_queue.get_correctly_ordered_middle_sum(print_orders)} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{print_queue.get_incorrectly_ordered_middle_sum(print_orders)} time: {time.time() - start}s")