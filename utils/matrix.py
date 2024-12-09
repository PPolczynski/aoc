class Matrix:
    def __init__(self, matrix, default=""):
        self._matrix = matrix
        if isinstance(matrix[0], str):
            self._matrix = [list(s) for s in matrix]
        self._default = default
        self.len_x = len(self._matrix[0])
        self.len_y = len(self._matrix)

    def __getitem__(self, coordinates: tuple[int, int]):
        x, y = coordinates
        return self._matrix[y][x] if not self.is_out_of_bounds(coordinates) else self._default

    def __setitem__(self, coordinates: tuple[int, int], value):
        x, y = coordinates
        if not self.is_out_of_bounds(coordinates):
            self._matrix[y][x] = value

    def iterate_row(self):
        for row in self._matrix:
            yield row

    def is_out_of_bounds(self, coordinates: tuple[int, int]) -> bool:
        x, y = coordinates
        return 0 > x or x >= self.len_x or 0 > y or y >= self.len_y

    def __iter__(self):
        self._y = -1
        self._x = -1
        return self

    def __next__(self):
        self._x += 1
        if self._x >= self.len_x:
            self._x = 0
            self._y += 1
        if self._y >= self.len_y:
            raise StopIteration
        return self._matrix[self._y][self._x], (self._x, self._y)

    def __str__(self):
        out = []
        for row in self._matrix:
            out.append(" ".join(str(value) for value in row))
        return "\n".join(out)

    @staticmethod
    def get_empty(len_x, len_y, empty_value, default=""):
        return Matrix([empty_value for _ in range(len_x)] * len_y, default=default)