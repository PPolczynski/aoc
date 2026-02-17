from puzzle import Solution

_empty_field = "."
_gear_symbol = "*"
_adjacent_fields = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
_adjacent_numbers_cnt_gear_ration = 2


def _part1(input_data: str) -> any:
    lines = input_data.splitlines()
    gear_schematic = GearSchematic(lines)
    return gear_schematic.get_sum_part_numbers()


def _part2(input_data: str) -> any:
    lines = input_data.splitlines()
    gear_schematic = GearSchematic(lines)
    return gear_schematic.get_sum_gear_ratio()


solution = Solution(
    "Gear Ratios",
    "3",
    "2023",
    part1=_part1,
    part2=_part2
)


class GearSchematic:
    def __init__(self, schematic: list[str]):
        self._schematic = schematic
        self._rows_cnt = len(self._schematic)
        self._columns_cnt = len(self._schematic[0])

    def get_sum_part_numbers(self) -> int:
        part_number_sum = 0
        buffer = ""
        symbol_detected = False
        for row_id, rows in enumerate(self._schematic):
            for column_id, column_value in enumerate(rows):
                if column_value.isnumeric():
                    buffer += column_value
                    symbol_detected = symbol_detected or self._has_symbol_adjacent(row_id, column_id)
                elif symbol_detected and buffer:
                    part_number_sum += int(buffer)
                    symbol_detected = False
                    buffer = ""
                else:
                    buffer = ""
        return part_number_sum

    def get_sum_gear_ratio(self) -> int:
        gear_ratio_sum = 0
        for row_id, rows in enumerate(self._schematic):
            for column_id, column_value in enumerate(rows):
                if column_value == _gear_symbol:
                    adjacent_numbers = self._get_adjacent_numbers(row_id, column_id)
                    if len(adjacent_numbers) == _adjacent_numbers_cnt_gear_ration:
                        gear_ratio_sum += adjacent_numbers[0] * adjacent_numbers[1]
        return gear_ratio_sum

    def _get_adjacent_numbers(self, row_id: int, column_id: int) -> list[int]:
        visited = set()
        numbers = []
        for row_offset, col_offset in _adjacent_fields:
            c_row_id, c_col_id = row_id + row_offset, column_id + col_offset
            if (c_row_id, c_col_id) not in visited:
                if not self._is_out_of_bounds(c_row_id, c_col_id) and self._schematic[c_row_id][c_col_id].isnumeric():
                    numbers.append(self._get_full_adjacent_number(c_row_id, c_col_id, visited))
                visited.add((c_row_id, c_col_id))
        return numbers

    def _get_full_adjacent_number(self, row_id: int, column_id: int, visited: set[tuple[int, int]]) -> int:
        buffer = self._schematic[row_id][column_id]
        column_offset = -1
        while ((row_id, column_id + column_offset) not in visited and
            not self._is_out_of_bounds(row_id, column_id + column_offset)
            and self._schematic[row_id][column_id + column_offset].isnumeric()):
            buffer = self._schematic[row_id][column_id + column_offset] + buffer
            visited.add((row_id, column_id + column_offset))
            column_offset -= 1
        column_offset = 1
        while ((row_id, column_id + column_offset) not in visited and
            not self._is_out_of_bounds(row_id, column_id + column_offset)
            and self._schematic[row_id][column_id + column_offset].isnumeric()):
            buffer += self._schematic[row_id][column_id + column_offset]
            visited.add((row_id, column_id + column_offset))
            column_offset += 1
        return int(buffer)

    def _has_symbol_adjacent(self, row_id: int, column_id: int) -> bool:
        for row_offset, col_offset in _adjacent_fields:
            if self._is_symbol(row_id + row_offset, column_id + col_offset):
                return True
        return False

    def _is_out_of_bounds(self, row_id: int, column_id: int) -> bool:
        if 0 > column_id or column_id >= self._columns_cnt or 0 > row_id or row_id >= self._rows_cnt:
            return True
        return False

    def _is_symbol(self, row_id: int, column_id: int) -> bool:
        if self._is_out_of_bounds(row_id, column_id):
            return False
        character = self._schematic[row_id][column_id]
        return character != _empty_field and not character.isnumeric()