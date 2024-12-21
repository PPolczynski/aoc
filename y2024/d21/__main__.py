import time

from y2024.d21.solution import get_codes_complexity

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())

    print("Part 1:")
    start = time.time()
    print(f"{(get_codes_complexity(lines, 2))} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{(get_codes_complexity(lines, 25))} time: {time.time() - start}s")