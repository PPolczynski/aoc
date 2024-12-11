_working = "."
_damaged = "#"
_unknown = "?"

class HotSprings:

    @staticmethod
    def get_arrangements_count(record: str) -> int:
        springs, groups = record.split()
        groups = list(map(int, groups.split(",")))
        return HotSprings._backtrack(0, 0, 0, springs, groups, dict())

    @staticmethod
    def get_arrangements_count_unfolded(record: str, unfold_times: int) -> int:
        springs, groups = record.split()
        springs = _unknown.join([springs for _ in range(unfold_times)])
        groups = list(map(int, groups.split(","))) * unfold_times
        result = HotSprings._backtrack(0, 0, 0, springs, groups, dict())
        return result

    @staticmethod
    def get_arrangements_count_in_records(records: list[str])  -> int:
        return sum([HotSprings.get_arrangements_count(record) for record in records])

    @staticmethod
    def get_arrangements_count_in_records_unfolded(records: list[str], unfold_times: int) -> int:
        return sum([HotSprings.get_arrangements_count_unfolded(record, unfold_times) for record in records])

    @staticmethod
    def _backtrack(current_group: int, idx_s: int, idx_r: int, springs: str, groups: list[int], mem: dict) -> int:
        if (idx_r, idx_s, current_group) in mem:
            return mem[(idx_r, idx_s, current_group)]
        elif idx_r >= len(groups):
            # if run out of groups check if there are damaged remaining
            mem[(idx_r, idx_s, current_group)] = 1 if springs.find(_damaged, idx_s) == -1 else 0
        elif idx_s >= len(springs):
            # if end of string check if all groups are used or one remain, and it is equal to number of current group
            mem[(idx_r, idx_s, current_group)] = 1 \
                if idx_r >= len(groups) or (idx_r == len(groups) - 1 and current_group == groups[idx_r]) else 0
        elif springs[idx_s] == _working:
            # if current group is empty go forward else check if ended group is valid
            if current_group == 0:
                mem[(idx_r, idx_s, current_group)] = (
                    HotSprings._backtrack(0, idx_s + 1, idx_r, springs, groups, mem))
            else:
                mem[(idx_r, idx_s, current_group)] = (
                    HotSprings._backtrack(0, idx_s + 1, idx_r + 1, springs, groups, mem)) \
                    if current_group == groups[idx_r] else 0
        elif springs[idx_s] == _damaged:
            mem[(idx_r, idx_s, current_group)] = (
                HotSprings._backtrack(current_group + 1, idx_s + 1, idx_r, springs, groups, mem))
        else: # Unknown
            total = 0
            if current_group == 0:
                total += HotSprings._backtrack(1, idx_s + 1, idx_r, springs, groups, mem)
                total += HotSprings._backtrack(0, idx_s + 1, idx_r, springs, groups, mem)
            elif current_group == groups[idx_r]:
                total += HotSprings._backtrack(0, idx_s + 1, idx_r + 1, springs, groups, mem)
            elif current_group > groups[idx_r]:
                mem[(idx_r, idx_s, current_group)] = 0
            else:
                total += HotSprings._backtrack(current_group + 1, idx_s + 1, idx_r, springs, groups, mem)
            mem[(idx_r, idx_s, current_group)] = total
        return  mem[(idx_r, idx_s, current_group)]