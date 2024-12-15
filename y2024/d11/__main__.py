import time

from y2024.d11.plutonian_pebbles import PlutonianPebbles

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())

    print("Part 1:")
    start = time.time()
    print(f"{PlutonianPebbles.count_stones(lines[0], 25)} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{PlutonianPebbles.count_stones(lines[0], 75)} time: {time.time() - start}s")
