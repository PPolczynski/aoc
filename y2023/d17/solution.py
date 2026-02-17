import heapq
from utils.matrix import Matrix
from puzzle import Solution

_adjacent_fields = [(1, 0), (-1, 0), (0, 1),  (0, -1)]
_max_steps_in_one_direction = 3

def _preprocess(input_data: str) -> list[str]:
    return input_data.splitlines()

def _part1(lines: list[str]) -> any:
    city_map = CityMap(lines)
    return city_map.get_least_heat_loss_possible(1, 3)

def _part2(lines: list[str]) -> any:
    city_map = CityMap(lines)
    return city_map.get_least_heat_loss_possible(4, 10)

solution = Solution(
    "Clumsy Crucible",
    "17",
    "2023",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)

class CityMap:
    def __init__(self, city_map: list[str]):
        self._city_map = Matrix(city_map)
        self._start = (0, 0)
        self._end = (self._city_map.len_x - 1, self._city_map.len_y - 1)

    def get_least_heat_loss_possible(self, minimum_steps, maximum_steps):
        queue = [(0, self._start, (0, 0), minimum_steps)]
        heapq.heapify(queue)
        visited = set()
        visited.add(self._start)
        while queue:
            loss, coordinate, last_direction, count = heapq.heappop(queue)
            if coordinate == self._end and count >= minimum_steps:
                return loss
            x, y = coordinate
            key = (coordinate, last_direction, count)
            if key in visited:
                continue
            visited.add(key)
            if count < minimum_steps:
                dx, dy = last_direction
                nxt = (x + dx, y + dy)
                nxt_count = count + 1
                if self._city_map.is_out_of_bounds(nxt):
                    continue
                heapq.heappush(queue, (loss + int(self._city_map[nxt]), nxt, last_direction, nxt_count))
            else:
                for direction in _adjacent_fields:
                    dx, dy = direction
                    nxt = (x + dx, y + dy)
                    nxt_count = count + 1 if direction == last_direction else 1
                    if (nxt_count > maximum_steps
                            or (last_direction[0] * -1 == dx and last_direction[1] * -1 == dy)
                            or self._city_map.is_out_of_bounds(nxt)):
                        continue
                    heapq.heappush(queue, (loss + int(self._city_map[nxt]), nxt, direction, nxt_count))