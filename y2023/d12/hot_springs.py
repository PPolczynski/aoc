_working = "."
_damaged = "#"
_unknown = "?"

class HotSprings:

    @staticmethod
    def get_arrangements_count(record: str) -> int:
        springs, groups = record.split()
        groups = list(map(int, groups.split(",")))
        return HotSprings._backtrack(0, springs, groups, 0, 0)

    @staticmethod
    def get_arrangements_count_unfolded(record: str, unfold_times: int) -> int:
        springs, groups = record.split()
        springs = "?".join([springs for _ in range(unfold_times)])
        groups = list(map(int, groups.split(","))) * unfold_times
        print(springs, groups)
        return HotSprings._backtrack(0, springs, groups, 0, 0)

    @staticmethod
    def get_arrangements_count_in_records(records: list[str]):
        return sum([HotSprings.get_arrangements_count(record) for record in records])

    @staticmethod
    def get_arrangements_count_in_records_unfolded(records: list[str], unfold_times: int):
        return sum([HotSprings.get_arrangements_count_unfolded(record, unfold_times) for record in records])

    @staticmethod
    def _backtrack(used, springs, record, idx_s, idx_r):
        if idx_r >= len(record):
            return 1 if springs.find(_damaged, idx_s) == -1 and springs.find(_unknown, idx_s) else 0
        elif idx_s >= len(springs):
            return 1 if idx_r >= len(record) or (idx_r == len(record) - 1 and used == record[idx_r]) else 0
        elif springs[idx_s] == _working:
            if used == 0:
                return HotSprings._backtrack(0, springs, record, idx_s + 1, idx_r)
            else:
                return HotSprings._backtrack(0, springs, record, idx_s + 1, idx_r + 1) if used == record[idx_r] else 0
        elif springs[idx_s] == _damaged:
            return HotSprings._backtrack(used + 1, springs, record, idx_s + 1, idx_r)
        else:
            total = 0
            if used == 0:
                total += HotSprings._backtrack(1, springs, record, idx_s + 1, idx_r)
                total += HotSprings._backtrack(0, springs, record, idx_s + 1, idx_r)
            elif used == record[idx_r]:
                total += HotSprings._backtrack(0, springs, record, idx_s + 1, idx_r + 1)
            else:
                total += HotSprings._backtrack(used + 1, springs, record, idx_s + 1, idx_r)
            return total