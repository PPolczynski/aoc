from puzzle import Solution


def _preprocess(data: str) -> list[list[int]]:
    return [[int(n) for n in line[:]] for line in data.splitlines()]


def max_subsequence_value(numbers: list[int]) -> int:
    first, second = 0, 0
    last_idx = len(numbers) - 1
    for idx, value in enumerate(numbers):
        if value > first and idx != last_idx:
            first = value
            second = 0
        elif value > second:
            second = value
    return first * 10 + second


def _part1(banks: list[list[int]]) -> int:
    return sum([max_subsequence_value(bank) for bank in banks])


def _part2(banks: list[list[int]]) -> int:
    return 0


solution = Solution("Lobby ", "3", "2025",
                    part1=_part1,
                    part2=_part2,
                    part1_preprocess=_preprocess,
                    part2_preprocess=_preprocess)
