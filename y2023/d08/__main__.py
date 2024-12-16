import time

from y2023.d08.solution import IslandMap

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())
    moves, _, *graph = lines
    island_map = IslandMap(graph)
    print("Part 1:")
    start = time.time()
    print(f"{island_map.get_steps_count(moves)} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{island_map.get_steps_count_ghost(moves)} time: {time.time() - start}s")
