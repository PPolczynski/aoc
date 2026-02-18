from puzzle import Solution

def _preprocess(input_data: str) -> str:
    return input_data.strip()

def _part1(stones: str) -> any:
    return BlinkingStones.count_stones(stones, 25)

def _part2(stones: str) -> any:
    return BlinkingStones.count_stones(stones, 75)

solution = Solution(
    "Plutonian Pebbles",
    "11",
    "2024",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)

class BlinkingStones:
    @staticmethod
    def count_stones(stones: str, number_of_blinks: int) -> int:
        total = 0
        mem = dict()
        for stone in stones.split(" "):
            total += BlinkingStones._blink_stone(stone, number_of_blinks, mem)
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
                new_stones = BlinkingStones._blink_stone("1", number_of_blinks - 1, mem)
            elif len(stone) % 2 == 0:
                mid = len(stone) // 2
                left_half = stone[:mid]
                right_half = stone[mid:].lstrip("0")
                new_stones =  (BlinkingStones._blink_stone(left_half, number_of_blinks - 1, mem)
                               + BlinkingStones._blink_stone(right_half if len(right_half) else "0", number_of_blinks - 1, mem))
            else:
                new_stones = BlinkingStones._blink_stone(str(int(stone) * 2024), number_of_blinks - 1, mem)
        if stone in mem:
            mem[stone][number_of_blinks] = new_stones
        else:
            mem[stone] = dict()
            mem[stone][number_of_blinks] = new_stones
        return new_stones
