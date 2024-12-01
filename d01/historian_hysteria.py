from collections import Counter


class HistorianHysteria:
    def __init__(self, list_a: list[int], list_b: list[int]):
        self._list_a = list_a
        self._list_b = list_b

    def get_list_distance(self) -> int:
        return sum([abs(a - b) for a, b in zip(sorted(self._list_a), sorted(self._list_b))])

    def get_list_similarity(self) -> int:
        cnt_list_b = Counter(self._list_b)
        return sum([num * cnt_list_b.get(num, 0) for num in self._list_a])


if __name__ == '__main__':
    l1 = []
    l2 = []
    split_characters = "   "
    with open("data", "r") as data_file:
        for line in data_file:
            values = line.rstrip().split(split_characters)
            l1.append(int(values[0]))
            l2.append(int(values[1]))
    if len(l1) == len(l2):
        hh = HistorianHysteria(l1, l2)
        result_a = hh.get_list_distance()
        print(result_a)
        result_b = hh.get_list_similarity()
        print(result_b)
