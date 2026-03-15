import math

from utils.range import Range


class Polygon:
    def __init__(self, vertices: list[tuple[int, int]]):
        self.vertices = vertices

    def edges(self):
        for i in range(len(self.vertices)):
            yield self.vertices[i], self.vertices[(i + 1) % len(self.vertices)]

    def _get_scanline_intersections(self, y: int) -> list[int]:
        intersections = []
        for (x1, y1), (x2, y2) in self.edges():
            # Skip horizontal edges for intersection calculation
            if y1 == y2:
                continue

            if (y1 <= y < y2) or (y2 <= y < y1):
                # Linear interpolation for the intersection x coordinate
                x_inter = x1 + (y - y1) * (x2 - x1) // (y2 - y1)
                intersections.append(x_inter)
        return sorted(intersections)

    def boundary_points(self) -> list[tuple[int, int]]:
        if not self.vertices:
            return []

        points = set()
        for (x1, y1), (x2, y2) in self.edges():
            dx, dy = x2 - x1, y2 - y1
            g = math.gcd(abs(dx), abs(dy))
            points.add((x1, y1))
            for j in range(1, g + 1):
                points.add((x1 + dx * j // g, y1 + dy * j // g))
        return list(points)

    def points(self) -> list[tuple[int, int]]:
        # https://en.wikipedia.org/wiki/Scanline_rendering
        if not self.vertices:
            return []

        min_y = min(p[1] for p in self.vertices)
        max_y = max(p[1] for p in self.vertices)

        points = set(self.boundary_points())

        for y in range(min_y, max_y + 1):
            intersections = self._get_scanline_intersections(y)

            for i in range(0, len(intersections) - 1, 2):  # step 2 to skip even intersections as they are outside
                for x in range(intersections[i], intersections[i + 1] + 1):
                    points.add((x, y))

        return list(points)

    def as_ranges(self) -> dict[int, list[Range]]:
        if not self.vertices:
            return {}

        min_y = min(p[1] for p in self.vertices)
        max_y = max(p[1] for p in self.vertices)

        # Group boundary points by y to efficiently create ranges
        y_to_x = dict()
        for x, y in self.boundary_points():
            if y not in y_to_x:
                y_to_x[y] = set()
            y_to_x[y].add(x)

        result = dict()
        for y in range(min_y, max_y + 1):
            row_ranges = []

            intersections = self._get_scanline_intersections(y)
            for i in range(0, len(intersections) - 1, 2):
                row_ranges.append(Range(intersections[i], intersections[i + 1]))

            # Add ranges from boundary points
            if y in y_to_x:
                for x in y_to_x[y]:
                    row_ranges.append(Range(x, x))

            if row_ranges:
                result[y] = Range.simplify_ranges(row_ranges, join_adjacent=True)

        return result
