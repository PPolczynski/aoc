import time

from y2023.d12.hot_springs import HotSprings

if __name__ == '__main__':
    records = []
    with open("data", "r") as data_file:
        for line in data_file:
            records.append(line.rstrip())

    print("Part 1:")
    start = time.time()
    print(f"{HotSprings.get_arrangements_count_in_records(records)} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{HotSprings.get_arrangements_count_in_records_unfolded(records, 5)} time: {time.time() - start}s")
