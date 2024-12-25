import time

from y2024.d15.solution import Warehouse
from y2024.d25.solution import Locks

if __name__ == '__main__':
    locks_and_keys = []
    with open("data", "r") as data_file:
        i = 0
        locks_and_keys.append([])
        for line in data_file:
            if line.rstrip() == "":
                i += 1
                locks_and_keys.append([])
            else:
                locks_and_keys[i].append(line.rstrip())

    locks = Locks(locks_and_keys)
    print("Part 1:")
    start = time.time()
    print(f"{locks.get_fitting_keys_count()} time: {time.time() - start}s")
    # print("Part 2:")
    # start = time.time()
    # warehouse.apply_moves(moves)
    # print(f"{warehouse.get_boxes_coordinates_sum()} time: {time.time() - start}s")

