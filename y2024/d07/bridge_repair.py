def concat(x: int, y: int) -> int:
    return int(f"{x}{y}")

class BridgeRepair:

    @staticmethod
    def get_sum_valid_targets(data: list[tuple[int, list[int]]]) -> int:
        return sum([target if BridgeRepair.is_valid(target, values) else 0 for target, values in data])

    @staticmethod
    def is_valid(target: int, values: list[int]) -> int:
        return BridgeRepair._is_valid(values[0], 1, target, values)

    @staticmethod
    def _is_valid(current_value: int, idx: int, target: int, values: list[int]) -> bool:
        if current_value > target:
            return False
        elif idx >= len(values):
            return current_value == target
        else:
            return (BridgeRepair._is_valid(current_value + values[idx], idx + 1, target, values)
                    or BridgeRepair._is_valid(current_value * values[idx], idx + 1, target, values))

    @staticmethod
    def get_sum_valid_targets_with_concat(data: list[tuple[int, list[int]]]) -> int:
        return sum([target if BridgeRepair.is_valid_with_concat(target, values) else 0
                    for target, values in data])

    @staticmethod
    def is_valid_with_concat(target: int, values: list[int]) -> int:
        return BridgeRepair._is_valid_with_concat(values[0], 1, target, values)

    @staticmethod
    def _is_valid_with_concat(current_value: int, idx: int, target: int, values: list[int]) -> bool:
        if current_value > target:
            return False
        elif idx >= len(values):
            return current_value == target
        else:
            return (BridgeRepair._is_valid_with_concat(current_value + values[idx], idx + 1, target, values)
                    or BridgeRepair._is_valid_with_concat(current_value * values[idx], idx + 1, target, values)
                    or BridgeRepair._is_valid_with_concat(concat(current_value, values[idx]), idx + 1, target, values))

    @staticmethod
    def get_sum_valid_found(data: list[tuple[int, list[int]]], is_with_concat: bool) -> int:
        return sum([target if BridgeRepair.is_valid_found(target, values, is_with_concat) else 0
                    for target, values in data])

    @staticmethod
    def is_valid_found(target: int, values: list[int], is_with_concat: bool) -> int:
        """
        found on the internet implemented for education
        """
        partials = {target}
        for value in reversed(values):
            tmp_partials = set()
            for partial in partials:
                str_partial = str(partial)
                str_value = str(value)
                if partial % value == 0:
                    tmp_partials.add(partial // value)
                if partial >= value:
                    tmp_partials.add(partial - value)
                if is_with_concat and partial > value and str_partial.endswith(str_value):
                    tmp_partials.add(int(str_partial[: len(str_partial) - len(str_value)]))
            partials = tmp_partials
        return 0 in partials