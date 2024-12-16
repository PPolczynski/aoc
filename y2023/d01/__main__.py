import time

from y2023.d01.solution import Trebuchet

if __name__ == '__main__':
    document = []
    with open("data", "r") as data_file:
        for line in data_file:
            document.append(line.rstrip())
    trebuchet = Trebuchet(document)
    print("Part 1:")
    start = time.time()
    print(f"{trebuchet.get_calibration()} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{trebuchet.get_calibration_spelled_out()} time: {time.time() - start}s")