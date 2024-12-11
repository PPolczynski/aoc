from collections import deque


class PlutonianPebbles:
    @staticmethod
    def count_stones(stones: str, number_of_blinks: int) -> int:
        total = 0
        mem = dict()
        for stone in stones.split(" "):
            total += PlutonianPebbles._blink_stone(stone, number_of_blinks, mem)
        return total

    @staticmethod
    def _blink_stone(stone: str, number_of_blinks: int, mem: dict) -> int:
        if stone in mem and number_of_blinks in mem[stone]:
            return mem[stone][number_of_blinks]
        new_stones = 0
        if number_of_blinks == 0:
            new_stones =  1
        else:
            if stone == "0":
                new_stones = PlutonianPebbles._blink_stone("1", number_of_blinks - 1, mem)
            elif len(stone) % 2 == 0:
                mid = len(stone) // 2
                left_half = stone[:mid]
                right_half = stone[mid:].lstrip("0")
                new_stones =  (PlutonianPebbles._blink_stone(left_half, number_of_blinks - 1, mem)
                        + PlutonianPebbles._blink_stone(right_half if len(right_half) else "0", number_of_blinks - 1, mem))
            else:
                new_stones = PlutonianPebbles._blink_stone(str(int(stone) * 2024), number_of_blinks - 1, mem)
        if stone in mem:
            mem[stone][number_of_blinks] = new_stones
        else:
            mem[stone] = dict()
            mem[stone][number_of_blinks] = new_stones
        return new_stones
