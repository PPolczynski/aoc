from utils.matrix import Matrix

_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
_edge_offset = [(0.5, -0.5), (0.5, 0.5), (-0.5, 0.5), (-0.5, -0.5)]

class Garden:
    def __init__(self, garden: list[str]):
        self.garden = Matrix(garden)

    def _get_regions_with_perimeter_length(self) -> list[tuple[list[tuple[int, int]], int]]:
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
        regions = self._get_regions_with_perimeter_length()
        return sum(len(region) * perimeter for region, perimeter in regions)

    def get_fencing_cost_bulk(self) -> int:
        regions = self._get_regions_with_perimeter_length()
        return sum(len(region) * self._get_sides_count(region) for region, _ in regions)

    @staticmethod
    def _get_sides_count(region: list[tuple[int, int]]) -> int:
        edges = set()
        # get all four edges of every point
        for x, y in region:
            for dx, dy in _edge_offset:
                edges.add((x + dx, y + dy))
        sides = 0
        for x, y in edges:
            edges_in_region = [1 if (x + dx, dy + y) in region else 0 for dx, dy in _edge_offset]
            neighbours_count = sum(edges_in_region)
            if neighbours_count == 4:
                '''
                NOT an edge
                A || A
                = +  =
                A || A
                '''
                continue
            elif neighbours_count == 1 or neighbours_count == 3:
                '''
                1)  A || .  3) A || .
                    = +  =     = +  =
                    . || .     A || A
                '''
                sides += 1
            elif neighbours_count == 2 and edges_in_region in [[1, 0, 1, 0], [0, 1, 0, 1]] :
                '''
                THIS    A || . or . || A  NOT THIS  . || .  or  A || A  or  A || . or . || A 
                 ->     = +  =    = +  =     ->     = +  =      = +  =      = +  =    = +  =
                        . || A    A || .            A || A      . || .      A || .    . || A
                '''
                sides += 2
        return sides

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