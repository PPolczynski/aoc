import time

from y2024.d22.solution import Secrets

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(int(line.rstrip()))

    print("Part 1:")
    start = time.time()
    print(f"{(Secrets.get_nth_secret_number_sum(lines, 2000))} time: {time.time() - start}s")
    print("Part 2:")
    start = time.time()
    print(f"{(Secrets.get_max_bananas_sum_after_n_secrets(lines, 2000))} time: {time.time() - start}s")