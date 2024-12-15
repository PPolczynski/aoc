import time

from y2024.d15.warehouse_woes import WarehouseWoes

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
    warehouse_woes = WarehouseWoes(warehouse)
    print("What is the sum of all boxes' GPS coordinates?")
    start = time.time()
    warehouse_woes.apply_moves(moves)
    print(f"{warehouse_woes.get_boxes_coordinates_sum()} time: {time.time() - start}s")

