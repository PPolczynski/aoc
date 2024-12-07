import time

from y2023.d09.mirage_maintenance import MirageMaintenance

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())

    mirage_maintenance = MirageMaintenance(lines)
    print("What is the sum of these extrapolated values?")
    start = time.time()
    print(f"{mirage_maintenance.get_extrapolated_values_sum()} time: {time.time() - start}s")
    print("What is the sum of these extrapolated values?")
    start = time.time()
    print(f"{mirage_maintenance.get_extrapolated_previous_values_sum()} time: {time.time() - start}s")
