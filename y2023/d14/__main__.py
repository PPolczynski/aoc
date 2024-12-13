import time

from y2023.d14.parabolic_reflector_dish import ParabolicReflectorDish

if __name__ == '__main__':
    platform = []
    with open("data", "r") as data_file:
        for line in data_file:
            platform.append(line.rstrip())

    parabolic_reflector_dish = ParabolicReflectorDish(platform)
    print("Afterward, what is the total load on the north support beams?")
    start = time.time()
    parabolic_reflector_dish.tilt_north()
    print(f"{parabolic_reflector_dish.get_total_load_north_beams()} time: {time.time() - start}s")
    parabolic_reflector_dish = ParabolicReflectorDish(platform)
    print("What number do you get after summarizing the new reflection line in each pattern in your notes?")
    start = time.time()
    parabolic_reflector_dish.perform_n_cycles(1000000000)
    print(f"{parabolic_reflector_dish.get_total_load_north_beams()} time: {time.time() - start}s")
