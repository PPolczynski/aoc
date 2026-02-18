from puzzle import Solution

_pin = "#"

def _preprocess(input_data: str) -> list[list[str]]:
    blocks = input_data.strip().split("\n\n")
    return [block.splitlines() for block in blocks]

def _part1(locks_and_keys: list[list[str]]) -> any:
    locks = Locks(locks_and_keys)
    return locks.get_fitting_keys_count()

def _part2(input_data: any) -> any:
    return "MERRY CHRISTMAS!"

solution = Solution(
    "Code Chronicle",
    "25",
    "2024",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)

class Locks:
    def __init__(self, locks_and_keys: list[list[str]]):
        self._keys = []
        self._locks = []
        for lock_or_key in locks_and_keys:
            number_of_pins = len(lock_or_key[0])
            schematic = [-1] * number_of_pins
            is_lock = lock_or_key[0][0] == _pin
            for row in lock_or_key:
                for col_idx, value in enumerate(row):
                    schematic[col_idx] += 1 if value == _pin else 0
            if is_lock:
                self._locks.append(schematic)
            else:
                self._keys.append(schematic)

    def get_fitting_keys_count(self):
        count = 0
        for lock in self._locks:
            for key in self._keys:
                count += 1 if all([l_p + k_p <= 5 for l_p, k_p in zip(lock, key)]) else 0
        return count
