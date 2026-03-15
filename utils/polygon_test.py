from unittest import TestCase
from utils.range import Range
from utils.polygon import Polygon

class TestPolygon(TestCase):
    def test_polygon_edges(self):
        vertices = [(0, 0), (2, 0), (1, 2)]
        edges = list(Polygon(vertices).edges())
        expected = [((0, 0), (2, 0)), ((2, 0), (1, 2)), ((1, 2), (0, 0))]
        self.assertEqual(edges, expected)

    def test_scanline_intersections(self):
        vertices = [(0, 0), (4, 0), (2, 4)]
        poly = Polygon(vertices)
        self.assertEqual(poly._get_scanline_intersections(2), [1, 3])
        self.assertEqual(poly._get_scanline_intersections(0), [0, 4])

    def test_boundary_points(self):
        vertices = [(0, 0), (2, 0), (2, 2), (0, 2)]
        points = Polygon(vertices).boundary_points()
        expected = [
            (0, 0), (1, 0), (2, 0),
            (2, 1), (2, 2), (1, 2),
            (0, 2), (0, 1)
        ]
        self.assertCountEqual(points, expected)

    def test_points_square(self):
        vertices = [(0, 0), (2, 0), (2, 2), (0, 2)]
        points = Polygon(vertices).points()
        expected = [
            (0, 0), (1, 0), (2, 0),
            (0, 1), (1, 1), (2, 1),
            (0, 2), (1, 2), (2, 2)
        ]
        self.assertCountEqual(points, expected)

    def test_points_triangle(self):
        vertices = [(0, 0), (2, 0), (0, 2)]
        points = Polygon(vertices).points()
        expected = [
            (0, 0), (1, 0), (2, 0),
            (0, 1), (1, 1),
            (0, 2)
        ]
        self.assertCountEqual(points, expected)

    def test_points_L(self):
        vertices = [(0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (0, 2)]
        points = Polygon(vertices).points()
        expected = [
            (0, 0), (1, 0), (2, 0),
            (0, 1), (1, 1), (2, 1),
            (0, 2), (1, 2)
        ]
        self.assertCountEqual(points, expected)

    def test_as_ranges(self):
        vertices = [(0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (0, 2)]
        expected = {
            0: [Range(0, 2)],
            1: [Range(0, 2)],
            2: [Range(0, 1)]
        }
        self.assertEqual(Polygon(vertices).as_ranges(), expected)
