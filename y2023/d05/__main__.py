import time

from y2023.d05.seed_fertilizer import SeedFertilizer

if __name__ == '__main__':
    almanac = []
    with open("data", "r") as data_file:
        for line in data_file:
            almanac.append(line.rstrip())
    seed_fertilizer = SeedFertilizer(almanac)
    start = time.time()
    print("What is the lowest location number that corresponds to any of the initial seed numbers?")
    end = time.time()
    print(f"{seed_fertilizer.get_lowest_location()} time: {time.time() - start}s")
    #
    # print("What is the lowest location number that corresponds to any of the initial seed numbers?")
    # start = time.time()
    # lowest = seed_fertilizer.get_lowest_location_seed_ranges()
    # end = time.time()
    # print(lowest, str(end - start) + " s")