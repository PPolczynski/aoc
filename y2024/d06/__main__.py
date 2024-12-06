from y2024.d06.guard_gallivant import GuardGallivant

if __name__ == '__main__':
    maze = []
    with open("data", "r") as data_file:
        for line in data_file:
            maze.append(line.rstrip())

    guard_gallivant = GuardGallivant(maze)
    print("How many distinct positions will the guard visit before leaving the mapped area?")
    print(guard_gallivant.get_guard_move_count())
    print("How many different positions could you choose for this obstruction?")
    print(guard_gallivant.get_possible_loop_count())