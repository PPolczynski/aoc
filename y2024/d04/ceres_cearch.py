_adjacent_fields = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
_diagonal_adjacent_fields = [(-1, 1), (1, 1),(1, -1), (-1, -1)]
_mas_combinations = ["MMSS", "SMMS", "SSMM", "MSSM"]
_x_mas_center = "A"

class CeresSearch:
    def __init__(self, puzzle: list[str]):
        self._puzzle = puzzle
        self._rows_cnt = len(puzzle)
        self._columns_cnt = len(puzzle[0])

    def get_occurrence_count(self, word: str) -> int:
        cnt = 0
        for row_id, rows in enumerate(self._puzzle):
            for column_id, char in enumerate(rows[:]):
                if char == word[0]:
                    for direction in _adjacent_fields:
                        if self._search_in_direction(row_id + direction[0], column_id + direction[1], direction, word, 1):
                            cnt += 1
        return cnt

    def get_x_mas_occurrence_count(self) -> int:
        cnt = 0
        for row_id, rows in enumerate(self._puzzle):
            for column_id, char in enumerate(rows[:]):
                if char == _x_mas_center and self._is_x_mas(row_id, column_id):
                   cnt += 1
        return cnt

    def _is_x_mas(self, row_id: int, column_id: int) -> bool:
        diagonal_adjacent_chars = []
        for offset_r, offset_c in _diagonal_adjacent_fields:
            if self._is_out_of_bounds(row_id + offset_r, column_id + offset_c):
                return False
            diagonal_adjacent_chars.append(self._puzzle[row_id + offset_r][column_id + offset_c])
        letters = "".join(diagonal_adjacent_chars)

        return any([letters == combination for combination in _mas_combinations])

    def _search_in_direction(self, row_id: int, column_id: int, direction : tuple[int, int], word :str, char_idx :int) -> bool:
        if char_idx >= len(word):
            return True
        elif self._is_out_of_bounds(row_id, column_id):
            return False
        elif self._puzzle[row_id][column_id] != word[char_idx]:
            return False
        else:
            return self._search_in_direction(row_id + direction[0], column_id + direction[1], direction, word, char_idx + 1)

    def _is_out_of_bounds(self, row_id: int, column_id: int) -> bool:
        if 0 > column_id or column_id >= self._columns_cnt or 0 > row_id or row_id >= self._rows_cnt:
            return True
        return False