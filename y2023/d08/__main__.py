import time

from y2023.d08.haunted_wasteland import HauntedWasteland

if __name__ == '__main__':
    lines = []
    with open("data", "r") as data_file:
        for line in data_file:
            lines.append(line.rstrip())
    moves, _, *graph = lines
    haunted_wasteland = HauntedWasteland(graph)
    print("How many steps are required to reach ZZZ?")
    start = time.time()
    print(f"{haunted_wasteland.get_steps_count(moves)} time: {time.time() - start}s")
    print("How many steps does it take before you're only on nodes that end with Z?")
    start = time.time()
    print(f"{haunted_wasteland.get_steps_count_ghost(moves)} time: {time.time() - start}s")
