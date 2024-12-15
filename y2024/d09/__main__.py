import time

from y2024.d09.disk_fragmenter import DiskFragmenter

if __name__ == '__main__':
    disk_space = []
    with open("data", "r") as data_file:
        for line in data_file:
            disk_space.append(line.rstrip())

    disk_fragment = DiskFragmenter(disk_space[0])
    print("Part 1:")
    start = time.time()
    print(f"{disk_fragment.get_fragemented_checksum()} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{disk_fragment.get_fragemented_files_checksum()} time: {time.time() - start}s")
