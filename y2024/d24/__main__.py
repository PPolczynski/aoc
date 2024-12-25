import time

from y2024.d24.solution import Gates

if __name__ == '__main__':
    known = []
    graph = []
    after_break = False
    with open("data", "r") as data_file:
        for line in data_file:
            l = line.rstrip()
            if l == "":
                after_break = True
            elif after_break:
                graph.append(l)
            else:
                known.append(l)

    gates = Gates(known, graph)
    print("Part 1:")
    start = time.time()
    print(f"{gates.get_z_gets_decimal()} time: {time.time() - start}s")
    gates = Gates(known, graph)
    print("Part 2:")
    start = time.time()
    #https://en.wikipedia.org/wiki/Adder_(electronics)
    #rules to follow to fix the graph manually
    print(f"{gates.part2()} time: {time.time() - start}s")

