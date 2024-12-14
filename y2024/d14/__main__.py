import time

from y2024.d14.restroom_redoubt import RestroomRedoubt

if __name__ == '__main__':
    robots = []
    with open("data", "r") as data_file:
        for line in data_file:
            robots.append(line.rstrip())

    restroom_redoubt = RestroomRedoubt(robots, 101, 103)
    print("What will the safety factor be after exactly 100 seconds have elapsed?")
    start = time.time()
    restroom_redoubt.pass_time(100)
    print(f"{restroom_redoubt.get_safety_factor()} time: {time.time() - start}s")
    # print(" What is the fewest tokens you would have to spend to win all possible prizes?")
    # start = time.time()
    # print(f"{claw_contraption.get_fewest_token_to_win_with_conversion(10000000000000)} time: {time.time() - start}s")
