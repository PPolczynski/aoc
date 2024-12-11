from utils.matrix import Matrix


class PointOfIncidence:

    @staticmethod
    def get_reflection(vulcano_map: list[str]):

        row = PointOfIncidence.search_for_reflection(vulcano_map)
        if row != -1:
            return row * 100

        column_organized = []
        for idx in range(len(vulcano_map[0])):
            column_organized.append([])
            for row in vulcano_map:
                column_organized[idx].append(row[idx])
        column_organized = ["".join(column) for column in column_organized]

        column = PointOfIncidence.search_for_reflection(column_organized)
        if column != -1:
            return column

    @staticmethod
    def search_for_reflection(rows) -> int:
        l = len(rows)
        previous = rows[0]
        for row_idx, line in enumerate(rows[1:]):
            if line == previous:
                i = row_idx + 1 # as we skip 1 idx is not off by 1 from rows
                j = 0
                while j < i and i + j < l:
                    if rows[i - j - 1] == rows[i + j]:
                        j += 1
                    else:
                        break
                else:
                    return i
            previous = line
        return -1

    @staticmethod
    def get_reflection_sum(vulcano_maps: list[list[str]]) -> int:
        total = 0
        for vulcano_map in vulcano_maps:
            total += PointOfIncidence.get_reflection(vulcano_map)
        return total