import time

from y2024.d15.solution import Warehouse

if __name__ == '__main__':
    warehouse_moves = []
    with open("data", "r") as data_file:
        i = 0
        warehouse_moves.append([])
        for line in data_file:
            if line.rstrip() == "":
                i += 1
                warehouse_moves.append([])
            else:
                warehouse_moves[i].append(line.rstrip())

    warehouse, moves = warehouse_moves
    warehouse_woes = Warehouse(warehouse)
    print("Part 1:")
    start = time.time()
    warehouse_woes.apply_moves(moves)
    print(f"{warehouse_woes.get_boxes_coordinates_sum()} time: {time.time() - start}s")
    warehouse_woes = Warehouse(warehouse, True)
    print("Part 2:")
    start = time.time()
    warehouse_woes.apply_moves(moves)
    print(f"{warehouse_woes.get_boxes_coordinates_sum()} time: {time.time() - start}s")

