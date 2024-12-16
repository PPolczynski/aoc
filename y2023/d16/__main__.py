import time
from y2023.d16.solution import Contraption

if __name__ == '__main__':
    contraption_lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            contraption_lines.append(line.rstrip())

    contraption = Contraption(contraption_lines)
    print("Part 1:")
    start = time.time()
    print(f"{contraption.get_energized_tiles_count((0, 0), (1, 0))} time: {time.time() - start}s")

    print("Part 2:")
    start = time.time()
    print(f"{contraption.get_max_energized_tiles_count()} time: {time.time() - start}s")
