from collections import Counter
from puzzle import Solution

def _preprocess(input_data: str) -> tuple[list[int], list[int]]:
    lines = input_data.splitlines()
    list_a, list_b = zip(*(map(int, line.split()) for line in lines))
    return list(list_a), list(list_b)

def _part1(lists: tuple[list[int], list[int]]) -> any:
    list_a, list_b = lists
    locations = Locations(list_a, list_b)
    return locations.get_list_distance()

def _part2(lists: tuple[list[int], list[int]]) -> any:
    list_a, list_b = lists
    locations = Locations(list_a, list_b)
    return locations.get_list_similarity()

solution = Solution(
    "Historian Hysteria",
    "1",
    "2024",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)

class Locations:
    def __init__(self, list_a: list[int], list_b: list[int]):
        self._list_a = list_a
        self._list_b = list_b

    def get_list_distance(self) -> int:
        return sum([abs(num_a - num_b) for num_a, num_b in zip(sorted(self._list_a), sorted(self._list_b))])

    def get_list_similarity(self) -> int:
        cnt_list_b = Counter(self._list_b)
        return sum([num_a * cnt_list_b.get(num_a, 0) for num_a in self._list_a])
