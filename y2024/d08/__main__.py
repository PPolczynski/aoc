import time

from y2024.d08.resonant_collinearity import ResonantCollinearity

if __name__ == '__main__':
    map = []
    with open("data", "r") as data_file:
        for line in data_file:
            map.append(line.rstrip())

    resonant_collinearity = ResonantCollinearity(map)
    print("How many unique locations within the bounds of the map contain an antinode?")
    start = time.time()
    print(f"{resonant_collinearity.get_antinodes_count()} time: {time.time() - start}s")
    print("How many unique locations within the bounds of the map contain an antinode?")
    start = time.time()
    print(f"{resonant_collinearity.get_antinodes_count_distance_multiplier()} time: {time.time() - start}s")
