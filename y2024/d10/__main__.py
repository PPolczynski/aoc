import time

from y2024.d10.hoof_it import HoofIt

if __name__ == '__main__':
    topo = []
    with open("data", "r") as data_file:
        for line in data_file:
            topo.append(line.rstrip())

    hoof_it = HoofIt(topo)
    print("What is the sum of the scores of all trailheads on your topographic map?")
    start = time.time()
    print(f"{hoof_it.get_trailheads_score_sum()} time: {time.time() - start}s")
    # print("What is the resulting filesystem checksum?")
    # start = time.time()
    # print(f"{disk_fragment.get_fragemented_files_checksum()} time: {time.time() - start}s")
