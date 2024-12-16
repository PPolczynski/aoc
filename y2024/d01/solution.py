from collections import Counter


class Locations:
    def __init__(self, list_a: list[int], list_b: list[int]):
        self._list_a = list_a
        self._list_b = list_b

    def get_list_distance(self) -> int:
        return sum([abs(num_a - num_b) for num_a, num_b in zip(sorted(self._list_a), sorted(self._list_b))])

    def get_list_similarity(self) -> int:
        cnt_list_b = Counter(self._list_b)
        return sum([num_a * cnt_list_b.get(num_a, 0) for num_a in self._list_a])
