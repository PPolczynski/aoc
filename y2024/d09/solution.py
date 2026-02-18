from utils.linked_list_node import LinkedListNode
from puzzle import Solution

_empty_space = "."

def _preprocess(input_data: str) -> str:
    return input_data.strip()

def _part1(disk_space_sizes: str) -> any:
    disk_space = DiskSpace(disk_space_sizes)
    return disk_space.get_fragemented_checksum()

def _part2(disk_space_sizes: str) -> any:
    disk_space = DiskSpace(disk_space_sizes)
    return disk_space.get_fragemented_files_checksum()

solution = Solution(
    "Disk Fragmenter",
    "9",
    "2024",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)

class DiskSpace:

    def __init__(self, disk_space_sizes: str):
        self._sizes = list(map(int, disk_space_sizes[:]))

    def get_fragemented_checksum(self) -> int:
        idx = 0
        is_file = True
        disk_space = []
        for size in self._sizes:
            label = idx if is_file else _empty_space
            for i in range(size):
                disk_space.append(label)
            idx += 1 if is_file else 0
            is_file = not is_file
        i = 0
        j = len(disk_space) - 1
        while i < j:
            if disk_space[i] != _empty_space:
                i += 1
            elif disk_space[j] == _empty_space:
                j -= 1
            else:
                disk_space[i] = disk_space[j]
                disk_space[j] = _empty_space
                i += 1
                j -= 1
        total = 0
        for pos in range(i + 1):
            total += pos * disk_space[pos]
        return total

    def get_fragemented_files_checksum(self):
        idx = 0
        is_file = True
        dummy = LinkedListNode(0, None, None)
        prev = dummy
        for size in self._sizes:
            label = idx if is_file else _empty_space
            node = LinkedListNode((size, is_file, label), None, prev)
            prev.next = node
            prev = node
            idx += 1 if is_file else 0
            is_file = not is_file
        dummy.next.previous = None
        head = dummy.next
        tail = prev
        cur_end = tail
        while cur_end:
            size, is_file, label = cur_end.value
            if is_file:
                cur = head
                while cur and cur != cur_end:
                    c_size, c_is_file, c_label = cur.value
                    if not c_is_file and c_size >= size:
                        tmp = cur_end.previous
                        left_over = c_size - size
                        if left_over == 0:
                            cur_end.swap(cur)
                        else:
                            cur_end.swap(cur)
                            cur.value = (size, c_is_file, c_label)
                            cur_end.insert_after(LinkedListNode((left_over, c_is_file, c_label), None, None))
                        cur_end = tmp
                        break
                    else:
                        cur = cur.next
                else:
                    cur_end = cur_end.previous
            else:
                cur_end = cur_end.previous
        cur = head
        total = 0
        i = 0
        while cur:
            size, is_file, label = cur.value
            if is_file:
                for idx in range(i, i + size):
                    total += idx * label
            i += size
            cur = cur.next
        return total
