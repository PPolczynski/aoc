class Locks:
    def __init__(self, locks_and_keys: list[list[str]]):
        self._keys = []
        self._locks = []
        print(locks_and_keys)
        for lock_or_key in locks_and_keys:
            number_of_pins = len(lock_or_key[0])
            schematic = [-1] * number_of_pins
            is_lock = lock_or_key[0][0] == "#"
            char_to_count = "#"
            for row in lock_or_key:
                for col_idx, value in enumerate(row):
                    schematic[col_idx] += 1 if value == char_to_count else 0
            if is_lock:
                self._locks.append(schematic)
            else:
                self._keys.append(schematic)

        print(self._locks)
        print(self._keys)

    def get_fitting_keys_count(self):
        count = 0
        for lock in self._locks:
            for key in self._keys:
                count += 1 if all([l_p + k_p <= 5 for l_p, k_p in zip(lock, key)]) else 0
        return count