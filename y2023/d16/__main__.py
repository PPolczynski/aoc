import time
from y2023.d16.the_floor_wil_be_lava import TheFloorWillBeLava

if __name__ == '__main__':
    contraption = []
    with open("data", "r") as data_file:
        for line in data_file:
            contraption.append(line.rstrip())

    the_floor_wil_be_lava = TheFloorWillBeLava(contraption)
    print("how many tiles end up being energized?")
    start = time.time()
    print(f"{the_floor_wil_be_lava.get_energized_tiles_count((0,0), (1,0))} time: {time.time() - start}s")

    print("How many tiles are energized in that configuration?")
    start = time.time()
    print(f"{the_floor_wil_be_lava.get_max_energized_tiles_count()} time: {time.time() - start}s")
