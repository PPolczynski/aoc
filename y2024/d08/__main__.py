import time

from y2024.d08.solution import CityMap

if __name__ == '__main__':
    map = []
    with open("data", "r") as data_file:
        for line in data_file:
            map.append(line.rstrip())

    city_map = CityMap(map)
    print("Part 1:")
    start = time.time()
    print(f"{city_map.get_antinodes_count()} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{city_map.get_antinodes_count_distance_multiplier()} time: {time.time() - start}s")
