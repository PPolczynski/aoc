import time

from y2024.d12.solution import Garden

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())

    garden = Garden(lines)
    print("Part 1:")
    start = time.time()
    print(f"{garden.get_fencing_cost()} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{garden.get_fencing_cost_bulk()} time: {time.time() - start}s")
