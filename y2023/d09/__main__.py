import time

from y2023.d09.solution import Sensor

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())

    sensor = Sensor(lines)
    print("Part 1:")
    start = time.time()
    print(f"{sensor.get_extrapolated_values_sum()} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{sensor.get_extrapolated_previous_values_sum()} time: {time.time() - start}s")
