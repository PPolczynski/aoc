import time

from y2023.d11.cosmic_expansion import CosmicExpansion

if __name__ == '__main__':
    galaxy_map = []
    with open("data", "r") as data_file:
        for line in data_file:
            galaxy_map.append(line.rstrip())

    cosmic_expansion = CosmicExpansion(galaxy_map)
    print("What is the sum of these lengths?")
    start = time.time()
    print(f"{cosmic_expansion.get_galaxy_distance_sum()} time: {time.time() - start}s")
    # print("How many tiles are enclosed by the loop?")
    # start = time.time()
    # print(f"{pipe_maze.get_enclosed_tile_count()} time: {time.time() - start}s")
