from y2024.d05.print_queue import PrintQueue

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

    print_queue = PrintQueue(rules)
    print("What do you get if you add up the middle page number from those correctly-ordered updates?")
    print(print_queue.get_correctly_ordered_middle_sum(print_orders))
    print("What do you get if you add up the middle page numbers after correctly ordering just those updates?")
    print(print_queue.get_incorrectly_ordered_middle_sum(print_orders))