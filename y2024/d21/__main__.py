import time

from y2024.d21.solution import Keypads

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())

    keypad = Keypads()
    print("Part 1:")
    start = time.time()
    print(f"{(keypad.get_codes_complexity(lines, 2))} time: {time.time() - start}s")
    print("Part 2:")
    keypad = Keypads() #clean up to not use previously computed values
    start = time.time()
    print(f"{(keypad.get_codes_complexity(lines, 25))} time: {time.time() - start}s")