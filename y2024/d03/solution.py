import re

_mul_instruction_pattern = "mul\(\d+,\d+\)"
_enable_instruction = "do()"
_disable_instruction = "don't()"

class Solution:
    @staticmethod
    def get_sum_of_multiplications(corrupted_memory: str) -> int:
        return sum([Solution._resolve_mul_instruction(instruction)
                    for instruction in Solution._get_multiplication_instructions(corrupted_memory)])

    @staticmethod
    def _get_multiplication_instructions(corrupted_memory: str) -> list[str]:
        matches = re.findall(_mul_instruction_pattern, corrupted_memory)
        return matches

    @staticmethod
    def _resolve_mul_instruction(instruction: str) -> int:
        a, b = Solution._get_numbers_from_multiplication_instructions(instruction)
        return a * b

    @staticmethod
    def _get_numbers_from_multiplication_instructions(instruction: str) -> tuple[int, int]:
        a, b = re.findall("\d+", instruction)
        return int(a), int(b)

    @staticmethod
    def get_sum_of_multiplications_conditional(corrupted_memory: str) -> int:
        sum_multiplications = 0
        for enabled_memory in Solution._get_enabled_memory_parts(corrupted_memory):
            for instruction in Solution._get_multiplication_instructions(enabled_memory):
                sum_multiplications += Solution._resolve_mul_instruction(instruction)
        return sum_multiplications

    @staticmethod
    def _get_enabled_memory_parts(corrupted_memory: str) -> list[str]:
        enabled_memory = []
        split_on_do = corrupted_memory.split(_enable_instruction)
        for dos in split_on_do:
            enabled_memory.append(dos.split(_disable_instruction)[0]) #ignore everything after first dont()
        return enabled_memory