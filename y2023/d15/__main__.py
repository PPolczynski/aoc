import time
from y2023.d15.lens_library import LensLibrary

if __name__ == '__main__':
    initialization_sequence = []
    with open("data", "r") as data_file:
        for line in data_file:
            initialization_sequence.append(line.rstrip())

    print("Part 1:")
    start = time.time()
    print(f"{LensLibrary.get_hash_initialization_sequence(initialization_sequence[0])} time: {time.time() - start}s")

    print("Part 2:")
    start = time.time()
    print(f"{LensLibrary.get_focusing_power_of_configuration(initialization_sequence[0])} time: {time.time() - start}s")
