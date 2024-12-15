import time

from y2024.d13.claw_contraption import ClawContraption

if __name__ == '__main__':
    machines = []
    with open("data", "r") as data_file:
        i = 0
        machines.append([])
        for line in data_file:
            if line.rstrip() == "":
                i += 1
                machines.append([])
            else:
                machines[i].append(line.rstrip())

    claw_contraption = ClawContraption(machines)
    print("Part 1:")
    start = time.time()
    print(f"{claw_contraption.get_fewest_token_to_win()} time: {time.time() - start}s")
    print(" Part 2:")
    start = time.time()
    print(f"{claw_contraption.get_fewest_token_to_win_with_conversion(10000000000000)} time: {time.time() - start}s")
