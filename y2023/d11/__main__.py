import time

from y2023.d11.cosmic_expansion import CosmicExpansion

if __name__ == '__main__':
    galaxy_map = []
    with open("data", "r") as data_file:
        for line in data_file:
            galaxy_map.append(line.rstrip())

    cosmic_expansion = CosmicExpansion(galaxy_map, 2)
    print("What is the sum of these lengths?")
    start = time.time()
    print(f"{cosmic_expansion.get_galaxy_distance_sum()} time: {time.time() - start}s")
    cosmic_expansion = CosmicExpansion(galaxy_map, 1000000)
    print("What is the sum of these lengths?")
    start = time.time()
    print(f"{cosmic_expansion.get_galaxy_distance_sum()} time: {time.time() - start}s")
