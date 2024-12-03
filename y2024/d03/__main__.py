from y2024.d03.mull_it_over import MullItOver

if __name__ == '__main__':
    corrupted_memory = []
    with open("data", "r") as data_file:
        for line in data_file:
            corrupted_memory.append(line.rstrip())

    print("What do you get if you add up all of the results of the multiplications?")
    print(sum([MullItOver.get_sum_of_multiplications(line) for line in corrupted_memory]))
    print("what do you get if you add up all of the results of just the enabled multiplications?")
    print(MullItOver.get_sum_of_multiplications_conditional("".join(corrupted_memory)))