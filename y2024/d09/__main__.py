import time

from y2024.d09.solution import DiskSpace

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())

    disk_space = DiskSpace(lines[0])
    print("Part 1:")
    start = time.time()
    print(f"{disk_space.get_fragemented_checksum()} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{disk_space.get_fragemented_files_checksum()} time: {time.time() - start}s")
