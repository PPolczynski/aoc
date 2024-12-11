import time

from y2023.d13.point_of_incidence import PointOfIncidence

if __name__ == '__main__':
    vulcano_maps = []
    with open("data", "r") as data_file:
        i = 0
        vulcano_maps.append([])
        for line in data_file:
            if line.rstrip() == "":
                i += 1
                vulcano_maps.append([])
            else:
                vulcano_maps[i].append(line.rstrip())

    print("What number do you get after summarizing all of your notes?")
    start = time.time()
    print(f"{PointOfIncidence.get_reflection_sum(vulcano_maps)} time: {time.time() - start}s")
    print("What number do you get after summarizing the new reflection line in each pattern in your notes?")
    start = time.time()
    print(f"{PointOfIncidence.get_reflection_sum_of_by(vulcano_maps, 1)} time: {time.time() - start}s")
