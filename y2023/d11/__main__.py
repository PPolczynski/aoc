import time

from y2023.d11.solution import GalaxyMap

if __name__ == '__main__':
    galaxy_map_lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            galaxy_map_lines.append(line.rstrip())

    galaxy_map = GalaxyMap(galaxy_map_lines, 2)
    print("Part 1:")
    start = time.time()
    print(f"{galaxy_map.get_galaxy_distance_sum()} time: {time.time() - start}s")
    galaxy_map = GalaxyMap(galaxy_map_lines, 1000000)
    print("Part 2:")
    start = time.time()
    print(f"{galaxy_map.get_galaxy_distance_sum()} time: {time.time() - start}s")
