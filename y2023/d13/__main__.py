import time

from y2023.d12.hot_springs import HotSprings
from y2023.d13.point_of_incidence import PointOfIncidence

if __name__ == '__main__':
    vulcano_maps = []
    with open("data", "r") as data_file:
        i = 0
        vulcano_maps.append([])
        for line in data_file:
            if line.rstrip() == "":
                i += 1
                vulcano_maps.append([])
            else:
                vulcano_maps[i].append(line.rstrip())

    print("What number do you get after summarizing all of your notes?")
    start = time.time()
    print(f"{PointOfIncidence.get_reflection_sum(vulcano_maps)} time: {time.time() - start}s")
    # print("What is the new sum of possible arrangement counts?")
    # start = time.time()
    # print(f"{HotSprings.get_arrangements_count_in_records_unfolded(records, 5)} time: {time.time() - start}s")
