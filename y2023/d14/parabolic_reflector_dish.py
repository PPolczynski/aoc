from utils.matrix import Matrix

_single_rock = "O"
_empty_space = "."

class ParabolicReflectorDish:
    def __init__(self, platform: list[str]):
        self._platform = Matrix(platform)

    def tilt_north(self):
        for x in range(self._platform.len_x):
            for y, row in enumerate(self._platform.iterate_row()):
                if row[x] == _single_rock:
                    i = y - 1
                    while (i >= 0
                        and not self._platform.is_out_of_bounds((x, i))
                        and self._platform[(x, i)] == _empty_space):
                        i -= 1
                    self._platform[(x, y)] = _empty_space
                    self._platform[(x, i + 1)] = _single_rock

    def get_total_load_north_beams(self) -> int:
        weight = 0
        for x, y in self._platform.find(_single_rock):
            weight += self._platform.len_y - y
        return weight