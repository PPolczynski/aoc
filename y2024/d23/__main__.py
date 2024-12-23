import time

from y2024.d23.solution import LanParty

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())

    lan_party = LanParty(lines)
    print("Part 1:")
    start = time.time()
    print(f"{(lan_party.get_group_connection_filtered())} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{(lan_party.get_largest_set())} time: {time.time() - start}s")