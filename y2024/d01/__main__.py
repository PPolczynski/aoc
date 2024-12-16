import time

from y2024.d01.solution import Locations

if __name__ == '__main__':
    list_a = []
    list_b = []
    split_characters = "   "
    with open("data", "r") as data_file:
        for line in data_file:
            values = line.rstrip().split(split_characters)
            list_a.append(int(values[0]))
            list_b.append(int(values[1]))
    if len(list_a) == len(list_b):
        locations = Locations(list_a, list_b)
        print("Part 1:")
        start = time.time()
        print(f"{locations.get_list_distance()} time: {time.time() - start}s")
        print("Part 2:")
        start = time.time()
        print(f"{locations.get_list_similarity()} time: {time.time() - start}s")
