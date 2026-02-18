from puzzle import Solution as BaseSolution
import re
from utils.linked_list_node import LinkedListNode

def _preprocess(input_data: str) -> str:
    return input_data.strip()

def _part1(input_data: str) -> any:
    return LensLibrary.get_hash_initialization_sequence(input_data)

def _part2(input_data: str) -> any:
    return LensLibrary.get_focusing_power_of_configuration(input_data)

solution = BaseSolution(
    "Lens Library",
    "15",
    "2023",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)

class LensLibrary:
    @staticmethod
    def get_hash(string: str) -> int:
        current_value = 0
        for char in string:
            current_value += ord(char)
            current_value *= 17
            current_value %= 256
        return current_value

    @staticmethod
    def get_hash_initialization_sequence(initialization_sequence: str) -> int:
        return sum([LensLibrary.get_hash(instruction)
                    for instruction in initialization_sequence.split(",")])

    @staticmethod
    def get_focusing_power_of_configuration(lens_configurations: str) -> int:
        boxes = dict()

        for lens_configurations in lens_configurations.split(","):
            label = re.findall(r"\w+", lens_configurations)[0]
            key = LensLibrary.get_hash(label)
            is_addition = lens_configurations.find("=") != -1
            lens = int(re.findall(r"\d+", lens_configurations)[0]) if is_addition else 0
            if key in boxes:
                current = boxes[key]
                while current.next and current.value[0] != label:
                    current = current.next
                if is_addition and current.value[0] == label:
                    current.value = (label, lens)
                elif is_addition:
                    current.insert_after(LinkedListNode((label, lens)))
                elif current.value[0] == label:
                    if not boxes[key].previous and not boxes[key].next:
                        del boxes[key]
                    elif boxes[key] == current:
                            boxes[key] = current.next
                            current.detach()
                    else:
                        current.detach()
            elif is_addition:
                node = LinkedListNode((label, lens))
                boxes[key] = node

        total_power = 0
        for box_idx in range(0, 256):
            if box_idx in boxes:
                head = boxes[box_idx]
                slot_idx = 1
                while head:
                    total_power += (box_idx + 1) * slot_idx * head.value[1]
                    slot_idx += 1
                    head = head.next
        return total_power

