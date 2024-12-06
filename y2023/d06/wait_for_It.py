import math
from math import isqrt


class WaitForIt:
    @staticmethod
    def get_product_ways_to_beat_time(races: list[tuple[int, int]]) -> int:
        product = 1
        for race_time, record in races:
            product *= WaitForIt.ways_to_beat_time(race_time, record)
        return product

    @staticmethod
    def ways_to_beat_time(race_time, distance) ->int:
        x1, x2 = WaitForIt._get_zero_points(race_time, distance)
        return math.ceil(x2) - math.floor(x1) - 1

    @staticmethod
    def get_distance(race_time: int, hold_time: int) -> int:
        return -1 * (hold_time ** 2) + (hold_time * race_time)

    @staticmethod
    def _get_delta(race_time: int, distance: int) -> int:
        return race_time ** 2 - 4 * distance

    @staticmethod
    def _get_zero_points(race_time, distance) -> tuple[float, float]:
        delta = WaitForIt._get_delta(race_time, distance)
        sqrt_delta = math.sqrt(delta)
        x1 = (-1 * race_time + sqrt_delta) / (-1 * 2)
        x2 = (-1 * race_time - sqrt_delta) / (-1 * 2)
        return x1, x2