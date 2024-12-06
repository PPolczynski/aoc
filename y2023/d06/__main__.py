import re
import time

from y2023.d06.wait_for_It import WaitForIt

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(re.findall("\d+", line.rstrip()))
    races = list(zip([int(x) for x in lines[0]], [int(x) for x in lines[1]]))
    wait_for_it = WaitForIt()
    print("What do you get if you multiply these numbers together?")
    start = time.time()
    print(f"{WaitForIt.get_product_ways_to_beat_time(races)} time: {time.time() - start}s")

    races = [(int("".join(lines[0])), int("".join(lines[1])))]
    print("How many ways can you beat the record in this one much longer race?")
    start = time.time()
    print(f"{WaitForIt.get_product_ways_to_beat_time(races)} time: {time.time() - start}s")