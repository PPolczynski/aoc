import unittest
from .matrix import Matrix


class MatrixTestCase(unittest.TestCase):
    def test_init_list_of_strings(self):
        m = Matrix(["abc", "def"])
        self.assertEqual(m.len_x, 3)
        self.assertEqual(m.len_y, 2)
        self.assertEqual(m._matrix, [['a', 'b', 'c'], ['d', 'e', 'f']])

    def test_init_list_of_lists(self):
        m = Matrix([[1, 2], [3, 4]])
        self.assertEqual(m.len_x, 2)
        self.assertEqual(m.len_y, 2)
        self.assertEqual(m._matrix, [[1, 2], [3, 4]])

    def test_getitem(self):
        m = Matrix(["abc", "def"], default=".")
        self.assertEqual(m[0, 0], 'a')
        self.assertEqual(m[2, 0], 'c')
        self.assertEqual(m[0, 1], 'd')
        self.assertEqual(m[2, 1], 'f')
        self.assertEqual(m[3, 0], '.')
        self.assertEqual(m[0, 2], '.')

    def test_setitem(self):
        m = Matrix(["abc", "def"])
        m[0, 0] = 'X'
        self.assertEqual(m[0, 0], 'X')
        m[2, 1] = 'Y'
        self.assertEqual(m[2, 1], 'Y')
        m[3, 0] = 'Z'  # out of bounds, should not crash
        self.assertEqual(m[3, 0], "")

    def test_is_out_of_bounds(self):
        m = Matrix(["abc", "def"])
        self.assertTrue(m.is_out_of_bounds((-1, 0)))
        self.assertTrue(m.is_out_of_bounds((3, 0)))
        self.assertTrue(m.is_out_of_bounds((0, -1)))
        self.assertTrue(m.is_out_of_bounds((0, 2)))
        self.assertFalse(m.is_out_of_bounds((0, 0)))
        self.assertFalse(m.is_out_of_bounds((2, 1)))

    def test_find(self):
        m = Matrix(["aba", "aca"])
        self.assertEqual(m.find('a'), [(0, 0), (2, 0), (0, 1), (2, 1)])
        self.assertEqual(m.find('b'), [(1, 0)])
        self.assertEqual(m.find('x'), [])

    def test_find_first(self):
        m = Matrix(["aba", "aca"])
        self.assertEqual(m.find_first('a'), (0, 0))
        self.assertEqual(m.find_first('c'), (1, 1))
        self.assertIsNone(m.find_first('x'))

    def test_adjacent(self):
        m = Matrix(["abc", "def", "ghi"])
        # (1, 1) is 'e'
        # neighbors: (0, 1) 'd', (1, 2) 'h', (2, 1) 'f', (1, 0) 'b'
        adj = list(m.adjacent((1, 1)))
        self.assertEqual(len(adj), 4)
        expected = [('d', (0, 1)), ('h', (1, 2)), ('f', (2, 1)), ('b', (1, 0))]
        self.assertCountEqual(adj, expected)

    def test_adjacent_diagonal(self):
        m = Matrix(["abc", "def", "ghi"])
        adj = list(m.adjacent((1, 1), include_diagonal=True))
        self.assertEqual(len(adj), 8)
        # 4 adjacent + 4 diagonal
        expected = [
            ('d', (0, 1)), ('h', (1, 2)), ('f', (2, 1)), ('b', (1, 0)),
            ('g', (0, 2)), ('i', (2, 2)), ('c', (2, 0)), ('a', (0, 0))
        ]
        self.assertCountEqual(adj, expected)

    def test_iterate(self):
        m = Matrix(["ab", "cd"])
        items = list(m)
        self.assertEqual(items, [('a', (0, 0)), ('b', (1, 0)), ('c', (0, 1)), ('d', (1, 1))])

    def test_str(self):
        m = Matrix(["ab", "cd"])
        self.assertEqual(str(m), "a b\nc d")

    def test_get_empty(self):
        m = Matrix.get_empty(2, 2, 0)
        self.assertEqual(m._matrix, [[0, 0], [0, 0]])


if __name__ == '__main__':
    unittest.main()
