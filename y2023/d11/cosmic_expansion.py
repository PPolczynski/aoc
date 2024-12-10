from utils.matrix import Matrix

_galaxy = "#"


class CosmicExpansion:
    def __init__(self, galaxy_map: list[str]):
        self._galaxy_map = self._get_expend_galaxy_map(galaxy_map)

    @staticmethod
    def _get_expend_galaxy_map(galaxy_map: list[str]) -> Matrix:
        column_to_expand = set()
        len_x = len(galaxy_map[0])
        for x in range(0, len_x):
            for row in galaxy_map:
                if row[x] == _galaxy:
                    break
            else:
                column_to_expand.add(x)
        out = []
        for row in galaxy_map:
             duplicate_row = True
             new_row = []
             for idx, cell in enumerate(row):
                 if cell == _galaxy:
                     duplicate_row = False
                 if idx in column_to_expand:
                     new_row.append(cell)
                 new_row.append(cell)
             if duplicate_row:
                 out.append("".join(new_row))
             out.append("".join(new_row))
        return Matrix(out)

    def _get_galaxies(self):
        return self._galaxy_map.find(_galaxy)

    def get_galaxy_distance_sum(self) -> int:
        galaxies = self._get_galaxies()
        total = 0
        for idx, galaxy in enumerate(galaxies):
            for other_galaxy in galaxies[idx + 1:]:
                total += abs(galaxy[0] - other_galaxy[0]) + abs(galaxy[1] - other_galaxy[1])
        return total
