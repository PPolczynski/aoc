import time
from y2023.d15.lens_library import LensLibrary

if __name__ == '__main__':
    initialization_sequence = []
    with open("data", "r") as data_file:
        for line in data_file:
            initialization_sequence.append(line.rstrip())

    print("What is the sum of the results?")
    start = time.time()
    print(f"{LensLibrary.get_hash_initialization_sequence(initialization_sequence[0])} time: {time.time() - start}s")

    print("What is the focusing power of the resulting lens configuration?")
    start = time.time()
    print(f"{LensLibrary.get_focusing_power_of_configuration(initialization_sequence[0])} time: {time.time() - start}s")
