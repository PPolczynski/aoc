import time

from y2023.d05.seed_fertilizer import SeedFertilizer

if __name__ == '__main__':
    almanac = []
    with open("data", "r") as data_file:
        for line in data_file:
            almanac.append(line.rstrip())
    seed_fertilizer = SeedFertilizer(almanac)
    start = time.time()
    print("Part 1:")
    end = time.time()
    print(f"{seed_fertilizer.get_lowest_location()} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{seed_fertilizer.get_lowest_location_seed_ranges()} time: {time.time() - start}s")