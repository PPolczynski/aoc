import time

from y2024.d15.solution import Warehouse
from y2024.d24.solution import Gates

if __name__ == '__main__':
    known = []
    graph = []
    after_break = False
    with open("data", "r") as data_file:
        for line in data_file:
            l = line.rstrip()
            if l == "":
                after_break = True
            elif after_break:
                graph.append(l)
            else:
                known.append(l)

    gates = Gates(known, graph)
    print("Part 1:")
    start = time.time()
    print(f"{gates.get_z_gets_decimal()} time: {time.time() - start}s")
    # print("Part 2:")
    # start = time.time()
    # warehouse.apply_moves(moves)
    # print(f"{warehouse.get_boxes_coordinates_sum()} time: {time.time() - start}s")

