import time

from y2024.d07.bridge_repair import BridgeRepair

if __name__ == '__main__':
    data = []
    with open("data", "r") as data_file:
        for line in data_file:
            target, values = line.rstrip().split(": ")
            data.append((int(target), list(map(int, values.split(" ")))))

    bridge_repair = BridgeRepair()
    print("What is their total calibration result?")
    start = time.time()
    print(f"{bridge_repair.get_sum_valid_targets(data)} time: {time.time() - start}s")
    print("What is their total calibration result?")
    start = time.time()
    print(f"{bridge_repair.get_sum_valid_targets_with_concat(data)} time: {time.time() - start}s")