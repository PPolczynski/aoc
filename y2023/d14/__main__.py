import time

from y2023.d14.solution import Reflector

if __name__ == '__main__':
    platform = []
    with open("data", "r") as data_file:
        for line in data_file:
            platform.append(line.rstrip())

    reflector = Reflector(platform)
    print("Part 1:")
    start = time.time()
    reflector.tilt_north()
    print(f"{reflector.get_total_load_north_beams()} time: {time.time() - start}s")
    reflector = Reflector(platform)
    print("Part 2:")
    start = time.time()
    reflector.perform_n_cycles(1000000000)
    print(f"{reflector.get_total_load_north_beams()} time: {time.time() - start}s")
