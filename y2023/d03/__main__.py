from y2023.d03.gear_ratios import GearRatios

if __name__ == '__main__':
    schematics = []
    with open("data", "r") as data_file:
        for line in data_file:
            schematics.append(line.rstrip())
    gear_ratios = GearRatios(schematics)
    print("What is the sum of all of the part numbers in the engine schematic?")
    print(gear_ratios.get_sum_part_numbers())
    print("What is the sum of all of the gear ratios in your engine schematic?")
    print(gear_ratios.get_sum_gear_ratio())