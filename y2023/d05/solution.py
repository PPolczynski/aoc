import math

from puzzle import Solution as Puzzle


def _preprocess(input_data: str) -> list[str]:
    return input_data.splitlines()


def _part1(lines: list[str]) -> any:
    almanac = Almanac(lines)
    return almanac.get_lowest_location()


def _part2(lines: list[str]) -> any:
    almanac = Almanac(lines)
    return almanac.get_lowest_location_seed_ranges()


solution = Puzzle(
    "If You Give A Seed A Fertilizer",
    "5",
    "2023",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)

class Almanac:
    def __init__(self, almanac: list[str]):
        self._seeds = list(map(int, almanac[0].split(": ")[1].split(" ")))

        def get_next_map_range(start_idx) -> tuple[int, int]:
            end_idx = start_idx + 1
            while almanac[end_idx] != "":
                end_idx += 1
            return start_idx, end_idx

        map_start, map_end = get_next_map_range(2)
        self._seed_to_soil = _AlmanacMap(almanac[map_start: map_end])
        map_start, map_end = get_next_map_range(map_end + 1)
        self._soil_to_fertilizer = _AlmanacMap(almanac[map_start: map_end])
        map_start, map_end = get_next_map_range(map_end + 1)
        self._fertilizer_to_water = _AlmanacMap(almanac[map_start: map_end])
        map_start, map_end = get_next_map_range(map_end + 1)
        self._water_to_light = _AlmanacMap(almanac[map_start: map_end])
        map_start, map_end = get_next_map_range(map_end + 1)
        self._light_to_temperature = _AlmanacMap(almanac[map_start: map_end])
        map_start, map_end = get_next_map_range(map_end + 1)
        self._temperature_to_humidity = _AlmanacMap(almanac[map_start: map_end])
        self._humidity_to_location = _AlmanacMap(almanac[map_end + 1:])


    def get_lowest_location(self) -> int:
        return min([self._translate_seed_to_location(seed) for seed in self._seeds])

    def get_lowest_location_seed_ranges(self) -> int:
        lowest_location = float('inf')
        for start, length in zip(self._seeds[::2], self._seeds[1::2]):
            out = self._translate_range_to_location((start, start + length))
            lowest_location = min(min([start for start, _ in out]), lowest_location)
        return lowest_location

    def _translate_range_to_location(self, in_range: tuple[int, int]) -> list[tuple[int, int]]:
        ranges = [in_range]
        def translate(fn, in_ranges):
            out = []
            for r in in_ranges:
                out += fn(r)
            return out
        ranges = translate(self._seed_to_soil.get_get_translated_range, ranges)
        ranges = translate(self._soil_to_fertilizer.get_get_translated_range, ranges)
        ranges = translate(self._fertilizer_to_water.get_get_translated_range, ranges)
        ranges = translate(self._water_to_light.get_get_translated_range, ranges)
        ranges = translate(self._light_to_temperature.get_get_translated_range, ranges)
        ranges = translate(self._temperature_to_humidity.get_get_translated_range, ranges)
        ranges = translate(self._humidity_to_location.get_get_translated_range, ranges)
        return ranges

    def _translate_seed_to_location(self, seed: int) -> int:
        soil = self._seed_to_soil.get_translated(seed)
        fertilizer = self._soil_to_fertilizer.get_translated(soil)
        water = self._fertilizer_to_water.get_translated(fertilizer)
        light = self._water_to_light.get_translated(water)
        temperature = self._light_to_temperature.get_translated(light)
        humidity = self._temperature_to_humidity.get_translated(temperature)
        location = self._humidity_to_location.get_translated(humidity)
        return location

class _AlmanacMap:
    def __init__(self, almanac_part: list[str]):
        self.description = almanac_part[0].split(" ")[0]
        self._ranges = []
        for line in almanac_part[1:]:
            to_start, from_start, elements = list(map(int, line.split(" ")))
            self._ranges.append((from_start, from_start + elements - 1, to_start, to_start + elements - 1))
        self._ranges.sort(key=lambda x: x[1])
        self.ranges = self._ranges

    def get_translated(self, value: int) -> int:
        if value < self._ranges[0][0] or value > self._ranges[-1][1]:
            return value
        left = 0
        right = len(self._ranges) - 1
        while left <= right:
            mid = math.floor((left + right) / 2)
            start, end, to_start, _ = self._ranges[mid]
            if start <= value <= end:
                 offset = value - start
                 return to_start + offset
            elif value < start:
                right = mid - 1
            else:
                left = mid + 1
        return value

    def get_get_translated_range(self, in_range: tuple[int, int]) -> list[tuple[int, int]]:
        in_start, in_end = in_range
        out = []
        if in_end < self._ranges[0][0] or in_start > self._ranges[-1][1]:
            return [(in_start, in_end)]
        for from_start, from_end, to_start, to_end in self._ranges:
            if in_start <= from_end and from_start <= in_end:
                if in_start < from_start:
                    out.append((in_start, from_start - 1))
                    in_start = from_start
                offset_start = in_start - from_start
                if in_end >= from_end:
                    in_start = in_end - (in_end - from_end - 1)
                    out.append((to_start + offset_start, to_end))
                else:
                    offset_end = from_end - in_end
                    out.append((to_start + offset_start, to_end - offset_end))
                    in_start = from_end
                    break
        if in_start <= in_end:
            out.append((in_start, in_end))
        return out

    def __str__(self) -> str:
        return self.description + ": " + ", ".join(
            ["(" + str(start) + ", " + str(end) + ", " + str(to) + ", " + str(to_end) +")" for start, end, to, to_end in self._ranges])