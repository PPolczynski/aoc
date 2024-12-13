import time

from y2024.d12.garden_groups import GardenGroups

if __name__ == '__main__':
    garden = []
    with open("data", "r") as data_file:
        for line in data_file:
            garden.append(line.rstrip())

    garden_groups = GardenGroups(garden)
    print("What is the total price of fencing all regions on your map?")
    start = time.time()
    print(f"{garden_groups.get_fencing_cost()} time: {time.time() - start}s")
    print("What is the new total price of fencing all regions on your map?")
    start = time.time()
    print(f"{garden_groups.get_fencing_cost_bulk()} time: {time.time() - start}s")
