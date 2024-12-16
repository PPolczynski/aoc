import time

from y2023.d03.solution import GearSchematic

if __name__ == '__main__':
    schematics = []
    with open("data", "r") as data_file:
        for line in data_file:
            schematics.append(line.rstrip())
    gear_schematic = GearSchematic(schematics)
    print("Part 1:")
    start = time.time()
    print(f"{gear_schematic.get_sum_part_numbers()} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{gear_schematic.get_sum_gear_ratio()} time: {time.time() - start}s")