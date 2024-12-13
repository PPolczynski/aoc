class LensLibrary:
    @staticmethod
    def holiday_ascii_string_helper_algorithm(string: str) -> int:
        current_value = 0
        for char in string:
            current_value += ord(char)
            current_value *= 17
            current_value %= 256
        return current_value

    @staticmethod
    def get_hash_initialization_sequence(initialization_sequence: str) -> int:
        return sum([LensLibrary.holiday_ascii_string_helper_algorithm(instruction)
                    for instruction in initialization_sequence.split(",")])
