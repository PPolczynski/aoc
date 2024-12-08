class Matrix:
    def __init__(self, matrix, default=""):
        self._matrix = matrix
        if isinstance(matrix[0], str):
            self._matrix = [list(s) for s in matrix]
        self._default = default
        self._rows_cnt = len(self._matrix)
        self._columns_cnt = len(self._matrix[0])
        self.len_y = len(self._matrix[0])
        self.len_x = len(self._matrix)


    def __getitem__(self, coordinates: tuple[int, int]):
        row_id, column_id = coordinates
        return self._matrix[row_id][column_id] if not self.is_out_of_bounds(coordinates) else self._default

    def __setitem__(self, coordinates: tuple[int, int], value):
        row_id, column_id = coordinates
        if not self.is_out_of_bounds(coordinates):
            self._matrix[row_id][column_id] = value


    def is_out_of_bounds(self, coordinates: tuple[int, int]) -> bool:
        row_id, column_id = coordinates
        return 0 > column_id or column_id >= self._columns_cnt or 0 > row_id or row_id >= self._rows_cnt

    def __iter__(self):
        self._i = -1
        return self

    def __next__(self):
        self._i += 1
        if self._i >= self._rows_cnt:
            raise StopIteration
        return self._matrix[self._i]

    def __str__(self):
        out = []
        for row in self._matrix:
            out.append(" ".join(str(value) for value in row))
        return "\n".join(out)