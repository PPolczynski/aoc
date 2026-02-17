import math
from collections import defaultdict
from utils.matrix import Matrix
from puzzle import Solution

def _get_distance(x1: int, y1: int, x2: int, y2: int):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def _preprocess(input_data: str) -> list[str]:
    return input_data.splitlines()

def _part1(map_lines: list[str]) -> any:
    city_map = CityMap(map_lines)
    return city_map.get_antinodes_count()

def _part2(map_lines: list[str]) -> any:
    city_map = CityMap(map_lines)
    return city_map.get_antinodes_count_distance_multiplier()

solution = Solution(
    "Resonant Collinearity",
    "8",
    "2024",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)

class CityMap:
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
                    antinode = CityMap.get_antinode(antenna, other)
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
                        antinode = CityMap.get_antinode(antenna, other, multiplier)
                        if not self._city_map.is_out_of_bounds(antinode):
                            antinodes.add(antinode)
                            multiplier += 1
                        else:
                            break
        return len(antinodes)

    def _get_antennas_grouped_by_frequency(self):
        all_antennas = defaultdict(list)
        for value, coordinates in self._city_map:
            if value != ".":
                all_antennas[value].append(coordinates)
        return all_antennas

    @staticmethod
    def get_antinode(a: tuple[int, int], b: tuple[int, int], distance_multiplier: int = 2) -> tuple[int, int]:
        x1, y1 = a
        x2, y2 = b
        distance = _get_distance(x1, y1, x2, y2)

        def get_coordinate(c1, c2, d):
            return c1 - ((d * (c1 - c2)) / distance)

        return (round(get_coordinate(x1, x2, distance_multiplier * distance)),
                round(get_coordinate(y1, y2, distance_multiplier * distance)))