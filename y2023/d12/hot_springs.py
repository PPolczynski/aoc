_working = "."
_damaged = "#"
_unknown = "?"

class HotSprings:

    @staticmethod
    def get_arrangements_count(record: str) -> int:
        springs, groups = record.split()
        groups = list(map(int, groups.split(",")))
        return HotSprings._backtrack([], springs, groups, 0)

    @staticmethod
    def get_arrangements_count_unfolded(record: str, unfold_times: int) -> int:
        springs, groups = record.split()
        springs = "?".join([springs for _ in range(unfold_times)])
        groups = list(map(int, groups.split(","))) * unfold_times
        print(springs, groups)
        return HotSprings._backtrack([], springs, groups, 0)

    @staticmethod
    def get_arrangements_count_in_records(records: list[str]):
        return sum([HotSprings.get_arrangements_count(record) for record in records])

    @staticmethod
    def get_arrangements_count_in_records_unfolded(records: list[str], unfold_times: int):
        return sum([HotSprings.get_arrangements_count_unfolded(record, unfold_times) for record in records])

    @staticmethod
    def _is_valid(springs, record):
        i = 0
        cnt = 0
        for spring in springs:
            if spring == _working and cnt > 0:
                if i >= len(record) or record[i] != cnt:
                    return False
                else:
                    cnt = 0
                    i += 1
            elif spring == _working:
                cnt = 0
            else:
                cnt += 1
        if cnt > 0:
            if i >= len(record) or record[i] != cnt:
                return False
            else:
                i += 1
        return i >= len(record)

    @staticmethod
    def _backtrack(current, springs, record, idx):
        if idx >= len(springs):
            return 1 if HotSprings._is_valid(current, record) else 0
        elif springs[idx] != _unknown:
            current.append(springs[idx])
            cnt = HotSprings._backtrack(current, springs, record, idx + 1)
            current.pop()
            return cnt
        else:
            total = 0
            for spring in [_working, _damaged]:
                current.append(spring)
                total += HotSprings._backtrack(current, springs, record, idx + 1)
                current.pop()
            return total