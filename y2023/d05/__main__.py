import time

from y2023.d05.solution import Almanac

if __name__ == '__main__':
    almanac_lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            almanac_lines.append(line.rstrip())
    almanac = Almanac(almanac_lines)
    start = time.time()
    print("Part 1:")
    end = time.time()
    print(f"{almanac.get_lowest_location()} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{almanac.get_lowest_location_seed_ranges()} time: {time.time() - start}s")