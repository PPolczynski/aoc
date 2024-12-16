from utils.matrix import Matrix

_galaxy = "#"

class GalaxyMap:
    def __init__(self, galaxy_map: list[str], extension_rate: int):
        self._galaxy_map = Matrix(galaxy_map)
        self._row_to_expand, self._column_to_expand = self._get_galaxy_map_extensions(galaxy_map)
        self._extension_rate = extension_rate

    @staticmethod
    def _get_galaxy_map_extensions(galaxy_map: list[str]) -> tuple[set, set]:
        column_to_expand = set()
        len_x = len(galaxy_map[0])
        for x in range(0, len_x):
            for row in galaxy_map:
                if row[x] == _galaxy:
                    break
            else:
                column_to_expand.add(x)
        row_to_expand = set()
        for row_id, row in enumerate(galaxy_map):
            if row.find(_galaxy) == -1:
                row_to_expand.add(row_id)
        return row_to_expand, column_to_expand

    def _get_galaxies(self):
        galaxies = []
        offset_y = 0
        for y, row in enumerate(self._galaxy_map.iterate_row()):
            offset_x = 0
            if y in self._row_to_expand:
                offset_y += 1
            for x, cell in enumerate(row):
                if x in self._column_to_expand:
                    offset_x += 1
                if cell == _galaxy:
                    galaxies.append((x + offset_x * (self._extension_rate - 1), y + offset_y * (self._extension_rate - 1)))


        return galaxies

    def get_galaxy_distance_sum(self) -> int:
        galaxies = self._get_galaxies()
        total = 0
        for idx, galaxy in enumerate(galaxies):
            for other_galaxy in galaxies[idx + 1:]:
                total += abs(galaxy[0] - other_galaxy[0]) + abs(galaxy[1] - other_galaxy[1])
        return total
