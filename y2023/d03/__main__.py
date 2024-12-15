import time

from y2023.d03.gear_ratios import GearRatios

if __name__ == '__main__':
    schematics = []
    with open("data", "r") as data_file:
        for line in data_file:
            schematics.append(line.rstrip())
    gear_ratios = GearRatios(schematics)
    print("Part 1:")
    start = time.time()
    print(f"{gear_ratios.get_sum_part_numbers()} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{gear_ratios.get_sum_gear_ratio()} time: {time.time() - start}s")