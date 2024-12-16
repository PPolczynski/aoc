class Solution:

    @staticmethod
    def get_reflection(vulcano_map: list[str]):
        row = Solution._search_for_reflection(vulcano_map)
        if row != -1:
            return row * 100

        column_organized = list(zip(*vulcano_map))
        column = Solution._search_for_reflection(column_organized)
        if column != -1:
            return column

    @staticmethod
    def get_reflection_of_by(vulcano_map: list[str], of_by: int):
        row = Solution._search_for_reflection_of_by(vulcano_map, of_by)
        if row != -1:
            return row * 100

        column_organized = list(zip(*vulcano_map))
        column = Solution._search_for_reflection_of_by(column_organized, of_by)
        if column != -1:
            return column

        return 0

    @staticmethod
    def _search_for_reflection(rows) -> int:
        for idx in range(1, len(rows)):
            upper = rows[:idx][::-1]
            lower = rows[idx:]
            smaller_len = min(len(upper), len(lower))
            if upper[:smaller_len] == lower[:smaller_len]:
                return idx
        return -1

    @staticmethod
    def _search_for_reflection_of_by(rows, of_by: int) -> int:
        for idx in range(1, len(rows)):
            upper = rows[:idx][::-1]
            lower = rows[idx:]
            smaller_len = min(len(upper), len(lower))
            if sum([sum([0 if u == l else 1 for u, l in zip(u_row, l_row)])
                    for u_row, l_row in zip(upper[:smaller_len], lower[:smaller_len])]) == of_by:
                return idx
        return -1

    @staticmethod
    def get_reflection_sum(vulcano_maps: list[list[str]]) -> int:
        total = 0
        for vulcano_map in vulcano_maps:
            total += Solution.get_reflection(vulcano_map)
        return total

    @staticmethod
    def get_reflection_sum_of_by(vulcano_maps: list[list[str]], of_by: int) -> int:
        total = 0
        for vulcano_map in vulcano_maps:
            total += Solution.get_reflection_of_by(vulcano_map, of_by)
        return total