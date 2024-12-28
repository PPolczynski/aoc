import time
from y2023.d17.solution import CityMap

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())

    city_map = CityMap(lines)
    print("Part 1:")
    start = time.time()
    print(f"{city_map.get_least_heat_loss_possible()} time: {time.time() - start}s")

    # print("Part 2:")
    # start = time.time()
    # print(f"{contraption.get_max_energized_tiles_count()} time: {time.time() - start}s")
