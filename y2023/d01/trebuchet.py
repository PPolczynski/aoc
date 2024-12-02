from utils.trie import Trie

_numbers_map = {
    "one" : "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}

class Trebuchet:
    def __init__(self, calibration_document: list[str]):
        self._calibration_document = calibration_document
        self.trie = Trie()
        self.inverted_trie = Trie()
        for key in _numbers_map.keys():
            self.trie.add_word(key)
            self.inverted_trie.add_word(key[::-1])

    def get_calibration(self) -> int:
        return sum([self._get_code_from_line(line) for line in self._calibration_document])

    def get_calibration_spelled_out(self) -> int:
        return sum([self._get_code_from_line_spelled_out(line) for line in self._calibration_document])

    @staticmethod
    def _get_code_from_line(line: str) -> int:
        code = 0
        for char in line:
            if char.isnumeric():
                code = int(char) * 10
                break
        for char in line[::-1]:
            if char.isnumeric():
                code += int(char)
                break
        return code

    def _get_code_from_line_spelled_out(self, line: str) -> int:
        code = 0
        tmp = ""
        for char in line:
            tmp += char
            if char.isnumeric():
                code = int(char) * 10
                break
            elif self.trie.has_word(tmp):
                code = int(_numbers_map[tmp]) * 10
                break
            while not len(self.trie.stats_with(tmp)):
                tmp = tmp[1:]
        tmp = ""
        for char in line[::-1]:
            tmp += char
            if char.isnumeric():
                code += int(char)
                break
            elif self.inverted_trie.has_word(tmp):
                code += int(_numbers_map[tmp[::-1]])
                break
            while not len(self.inverted_trie.stats_with(tmp)):
                tmp = tmp[1:]
        return code