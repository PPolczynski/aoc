from utils.matrix import Matrix

_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class GardenGroups:
    def __init__(self, garden: list[str]):
        self.garden = Matrix(garden)

    def _get_regions_with_perimeter(self) -> list[tuple[list[tuple[int, int]], int]]:
        regions = []
        visited = set()
        for crop, coordinate in self.garden:
            if not coordinate in visited:
                region = set()
                perimeter = self._get_region(crop, coordinate, region)
                visited |= region
                regions.append((list(region), perimeter))
        return regions

    def get_fencing_cost(self) -> int:
        regions = self._get_regions_with_perimeter()
        return sum(len(region) * perimeter for region, perimeter in regions)

    def _get_region(self, crop: str, coordinate: tuple[int, int], region: set) -> int:
        if coordinate in region:
            return 0
        elif (self.garden.is_out_of_bounds(coordinate)
                or self.garden[coordinate] != crop):
            return 1
        else:
            region.add(coordinate)
            x, y = coordinate
            perimeter = 0
            for dx, dy in _directions:
                perimeter += self._get_region(crop, (x + dx, y + dy), region)
            return perimeter
