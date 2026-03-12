import heapq
import math
import re

from puzzle import Solution

_N_LARGEST_CIRCUITS = 3


def _preprocess(data: str) -> list[tuple[int, int, int]]:
    pattern = r"\d+"
    return [(int(x), int(y), int(z)) for x, y, z in [re.findall(pattern, line) for line in data.splitlines()]]


def distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


def _part1(boxes: list[tuple[int, int, int]]) -> int:
    connections = []
    for idx, box in enumerate(boxes):
        for other_box in boxes[idx + 1:]:
            connections.append((distance(box, other_box), box, other_box))
    heapq.heapify(connections)
    circuits, point_circuit_id = dict(), dict()
    next_circuit_id = 0
    for _ in range(1000):
        if len(connections) == 0:
            raise RuntimeError("malformed input: not enough connections")
        l, a, b = heapq.heappop(connections)
        if (a in point_circuit_id) != (b in point_circuit_id):
            circuit_id = point_circuit_id[a] if a in point_circuit_id else point_circuit_id[b]
            circuits[circuit_id] |= {a, b}
            point_circuit_id[a], point_circuit_id[b] = circuit_id, circuit_id
        elif a in point_circuit_id and b in point_circuit_id:
            if point_circuit_id[a] == point_circuit_id[b]:  # already connected indirectly
                continue
            a_id, b_id = point_circuit_id[a], point_circuit_id[b]
            circuits[a_id] = circuits[a_id] | circuits[b_id]
            for point in circuits[b_id]:
                point_circuit_id[point] = a_id
            del circuits[b_id]
        else:
            circuits[next_circuit_id] = {a, b}
            point_circuit_id[a], point_circuit_id[b] = next_circuit_id, next_circuit_id
            next_circuit_id += 1
    lengths = [len(circuits[key]) for key in circuits.keys()]
    heapq.heapify(lengths)
    out = 1
    for l in heapq.nlargest(_N_LARGEST_CIRCUITS, lengths):
        out *= l
    return out


def _part2(boxes: list[tuple[int, int, int]]) -> int:
    connections = []
    for idx, box in enumerate(boxes):
        for other_box in boxes[idx + 1:]:
            connections.append((distance(box, other_box), box, other_box))
    heapq.heapify(connections)
    circuits, point_circuit_id = dict(), dict()
    next_circuit_id = 0
    number_of_boxes, last_connection = len(boxes), ((-1, -1, -1), (-1, -1, -1))
    while len(connections) > 0:
        l, a, b = heapq.heappop(connections)
        if (a in point_circuit_id) != (b in point_circuit_id):
            circuit_id = point_circuit_id[a] if a in point_circuit_id else point_circuit_id[b]
            circuits[circuit_id] |= {a, b}
            point_circuit_id[a], point_circuit_id[b] = circuit_id, circuit_id
        elif a in point_circuit_id and b in point_circuit_id:
            if point_circuit_id[a] == point_circuit_id[b]:  # already connected indirectly
                continue
            a_id, b_id = point_circuit_id[a], point_circuit_id[b]
            circuits[a_id] = circuits[a_id] | circuits[b_id]
            for point in circuits[b_id]:
                point_circuit_id[point] = a_id
            del circuits[b_id]
            if len(point_circuit_id) == number_of_boxes and len(circuits) == 1:
                last_connection = (a, b)
                break
        else:
            circuits[next_circuit_id] = {a, b}
            point_circuit_id[a], point_circuit_id[b] = next_circuit_id, next_circuit_id
            next_circuit_id += 1
    return last_connection[0][0] * last_connection[1][0]


solution = Solution("Playground", "8", "2025",
                    part1=_part1,
                    part2=_part2,
                    part1_preprocess=_preprocess,
                    part2_preprocess=_preprocess)
