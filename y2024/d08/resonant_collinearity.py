import math
from collections import defaultdict

from utils.matrix import Matrix

def _get_distance(x1: int, y1: int, x2: int, y2: int):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

class ResonantCollinearity:
    def __init__(self, city_map: list[str]):
        self._city_map = Matrix(city_map)
    
    def get_antinodes_count(self) -> int:
        all_antennas = self._get_antennas_grouped_by_frequency()
        antinodes = set()
        for key in all_antennas.keys():
            antennas = all_antennas[key]
            if len(antennas) == 1:
                continue
            for i in range(len(antennas)):
                antenna = antennas[i]
                for j, other in enumerate(antennas):
                    if i == j:
                        continue
                    antinode = ResonantCollinearity.get_antinode(antenna, other)
                    if not self._city_map.is_out_of_bounds(antinode):
                        antinodes.add(antinode)
        return len(antinodes)

    def get_antinodes_count_distance_multiplier(self) -> int:
        all_antennas = self._get_antennas_grouped_by_frequency()
        antinodes = set()
        for key in all_antennas.keys():
            antennas = all_antennas[key]
            if len(antennas) == 1:
                continue
            for i in range(len(antennas)):
                antenna = antennas[i]
                for j, other in enumerate(antennas):
                    if i == j:
                        continue
                    antinodes.add(other) #other antenna is always a antinode
                    multiplier = 2
                    while True:
                        antinode = ResonantCollinearity.get_antinode(antenna, other, multiplier)
                        if not self._city_map.is_out_of_bounds(antinode):
                            antinodes.add(antinode)
                            multiplier += 1
                        else:
                            break
        return len(antinodes)

    def _get_antennas_grouped_by_frequency(self):
        all_antennas = defaultdict(list)
        for row_id, row in enumerate(self._city_map):
            for column_id, column in enumerate(row):
                if column != ".":
                    all_antennas[column].append((row_id, column_id))
        return all_antennas

    @staticmethod
    def get_antinode(a: tuple[int, int], b: tuple[int, int], distance_multiplier: int = 2) -> tuple[int, int]:
        y1, x1 = a
        y2, x2 = b
        distance = _get_distance(x1, y1, x2, y2)

        def get_coordinate(c1, c2, d):
            return c1 - ((d * (c1 - c2)) / distance)

        return (round(get_coordinate(y1, y2, distance_multiplier * distance)),
                round(get_coordinate(x1, x2, distance_multiplier * distance)))