import time

from y2023.d12.hot_springs import HotSprings

if __name__ == '__main__':
    records = []
    with open("data", "r") as data_file:
        for line in data_file:
            records.append(line.rstrip())

    print("What is the sum of these lengths?")
    start = time.time()
    print(f"{HotSprings.get_arrangements_count_in_records(records)} time: {time.time() - start}s")
    # print("What is the sum of these lengths?")
    # start = time.time()
    # print(f"{cosmic_expansion.get_galaxy_distance_sum()} time: {time.time() - start}s")
