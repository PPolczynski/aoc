import time

from y2024.d10.hoof_it import HoofIt

if __name__ == '__main__':
    topo = []
    with open("data", "r") as data_file:
        for line in data_file:
            topo.append(line.rstrip())

    hoof_it = HoofIt(topo)
    print("Part 1:")
    start = time.time()
    print(f"{hoof_it.get_trailheads_score_sum()} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{hoof_it.get_trailheads_score_distinct_paths_sum()} time: {time.time() - start}s")
