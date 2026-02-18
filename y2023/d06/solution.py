import math
import re

from puzzle import Solution as Puzzle

def _preprocess(data: str):
    lines = []
    for line in data.splitlines():
        lines.append(re.findall(r"\d+", line.rstrip()))
    races = list(zip([int(x) for x in lines[0]], [int(x) for x in lines[1]]))
    return races

def _preprocess_part2(data: str):
    lines = []
    for line in data.splitlines():
        lines.append(re.findall(r"\d+", line.rstrip()))
    races = [(int("".join(lines[0])), int("".join(lines[1])))]
    return races

def _part1(races) -> any:
    return Solution.get_product_ways_to_beat_time(races)


def _part2(races) -> any:
    return Solution.get_product_ways_to_beat_time(races)


solution = Puzzle(
    "Wait For It",
    "6",
    "2023",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess_part2
)
class Solution:
    @staticmethod
    def get_product_ways_to_beat_time(races: list[tuple[int, int]]) -> int:
        product = 1
        for race_time, record in races:
            product *= Solution.ways_to_beat_time(race_time, record)
        return product

    @staticmethod
    def ways_to_beat_time(race_time, distance) ->int:
        x1, x2 = Solution._get_zero_points(race_time, distance)
        return math.ceil(x2) - math.floor(x1) - 1

    @staticmethod
    def get_distance(race_time: int, hold_time: int) -> int:
        return -1 * (hold_time ** 2) + (hold_time * race_time)

    @staticmethod
    def _get_delta(race_time: int, distance: int) -> int:
        return race_time ** 2 - 4 * distance

    @staticmethod
    def _get_zero_points(race_time, distance) -> tuple[float, float]:
        delta = Solution._get_delta(race_time, distance)
        sqrt_delta = math.sqrt(delta)
        x1 = (-1 * race_time + sqrt_delta) / (-1 * 2)
        x2 = (-1 * race_time - sqrt_delta) / (-1 * 2)
        return x1, x2