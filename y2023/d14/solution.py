from utils.matrix import Matrix
from puzzle import Solution

_single_rock = "O"
_empty_space = "."

def _preprocess(input_data: str) -> list[str]:
    return input_data.splitlines()

def _part1(platform: list[str]) -> any:
    reflector = Reflector(platform)
    reflector.tilt_north()
    return reflector.get_total_load_north_beams()

def _part2(platform: list[str]) -> any:
    reflector = Reflector(platform)
    reflector.perform_n_cycles(1000000000)
    return reflector.get_total_load_north_beams()

solution = Solution(
    "Parabolic Reflector Dish",
    "14",
    "2023",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)

class Reflector:
    def __init__(self, platform: list[str]):
        self._platform = Matrix(platform)

    def tilt_north(self) -> None:
        for x in range(self._platform.len_x):
            for y, row in enumerate(self._platform.iterate_row()):
                if row[x] == _single_rock:
                    i = y - 1
                    while (not self._platform.is_out_of_bounds((x, i))
                        and self._platform[(x, i)] == _empty_space):
                        i -= 1
                    self._platform[(x, y)] = _empty_space
                    self._platform[(x, i + 1)] = _single_rock

    def tilt_west(self) -> None:
        for y, row in enumerate(self._platform.iterate_row()):
            for x, cell in enumerate(row):
                if cell == _single_rock:
                    i = x - 1
                    while (not self._platform.is_out_of_bounds((i, y))
                        and self._platform[(i, y)] == _empty_space):
                        i -= 1
                    self._platform[(x, y)] = _empty_space
                    self._platform[(i + 1), y] = _single_rock

    def tilt_south(self) -> None:
        for x in range(self._platform.len_x):
            for y in range(self._platform.len_y - 1, -1 , -1):
                if self._platform[(x, y)] == _single_rock:
                    i = y + 1
                    while (not self._platform.is_out_of_bounds((x, i))
                        and self._platform[(x, i)] == _empty_space):
                        i += 1
                    self._platform[(x, y)] = _empty_space
                    self._platform[(x, i - 1)] = _single_rock

    def tilt_east(self) -> None:
        for y, row in enumerate(self._platform.iterate_row()):
            for x in range(self._platform.len_x - 1, -1, -1):
                if self._platform[(x, y)] == _single_rock:
                    i = x + 1
                    while (not self._platform.is_out_of_bounds((i, y))
                        and self._platform[(i, y)] == _empty_space):
                        i += 1
                    self._platform[(x, y)] = _empty_space
                    self._platform[(i - 1), y] = _single_rock

    def perform_n_cycles(self, n: int) -> None:
        mem = dict()
        cnt = 0
        cycle_found = False
        while cnt <= n - 1:
            self.perform_cycle()
            picture = "".join(["".join(row) for row in self._platform.iterate_row()]) if not cycle_found else ""
            if not cycle_found and picture in mem:
                cycle_found = True
                cycle_length = cnt - mem[picture]
                remaining = n - 1 - cnt
                cnt = n - remaining % cycle_length
                continue
            mem[picture] = cnt
            cnt += 1

    def perform_cycle(self) -> None:
        self.tilt_north()
        self.tilt_west()
        self.tilt_south()
        self.tilt_east()

    def get_total_load_north_beams(self) -> int:
        weight = 0
        for x, y in self._platform.find(_single_rock):
            weight += self._platform.len_y - y
        return weight