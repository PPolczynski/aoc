import re
from puzzle import Solution as BaseSolution

_mul_instruction_pattern = r"mul\(\d+,\d+\)"
_enable_instruction = "do()"
_disable_instruction = "don't()"

def _preprocess_part1(input_data: str) -> list[str]:
    return input_data.splitlines()

def _preprocess_part2(input_data: str) -> str:
    return input_data.replace("\n", "")

def _part1(lines: list[str]) -> any:
    return sum([MullItOver.get_sum_of_multiplications(line) for line in lines])

def _part2(data: str) -> any:
    return MullItOver.get_sum_of_multiplications_conditional(data)

solution = BaseSolution(
    "Mull It Over",
    "3",
    "2024",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess_part1,
    part2_preprocess=_preprocess_part2
)

class MullItOver:
    @staticmethod
    def get_sum_of_multiplications(corrupted_memory: str) -> int:
        return sum([MullItOver._resolve_mul_instruction(instruction)
                    for instruction in MullItOver._get_multiplication_instructions(corrupted_memory)])

    @staticmethod
    def _get_multiplication_instructions(corrupted_memory: str) -> list[str]:
        matches = re.findall(_mul_instruction_pattern, corrupted_memory)
        return matches

    @staticmethod
    def _resolve_mul_instruction(instruction: str) -> int:
        a, b = MullItOver._get_numbers_from_multiplication_instructions(instruction)
        return a * b

    @staticmethod
    def _get_numbers_from_multiplication_instructions(instruction: str) -> tuple[int, int]:
        a, b = re.findall(r"\d+", instruction)
        return int(a), int(b)

    @staticmethod
    def get_sum_of_multiplications_conditional(corrupted_memory: str) -> int:
        sum_multiplications = 0
        for enabled_memory in MullItOver._get_enabled_memory_parts(corrupted_memory):
            for instruction in MullItOver._get_multiplication_instructions(enabled_memory):
                sum_multiplications += MullItOver._resolve_mul_instruction(instruction)
        return sum_multiplications

    @staticmethod
    def _get_enabled_memory_parts(corrupted_memory: str) -> list[str]:
        enabled_memory = []
        split_on_do = corrupted_memory.split(_enable_instruction)
        for dos in split_on_do:
            enabled_memory.append(dos.split(_disable_instruction)[0]) #ignore everything after first dont()
        return enabled_memory