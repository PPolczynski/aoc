import unittest

from y2024.d09.disk_fragmenter import DiskFragmenter


class DiskFragmenterTestCase(unittest.TestCase):
    def test_get_fragemented_checksum(self):
        disk_space = "2333133121414131402"
        disk_fragment = DiskFragmenter(disk_space)
        self.assertEqual(1928, disk_fragment.get_fragemented_checksum())

    def test_get_fragemented_files_checksum(self):
        disk_space = "2333133121414131402"
        disk_fragment = DiskFragmenter(disk_space)
        self.assertEqual(2858, disk_fragment.get_fragemented_files_checksum())

if __name__ == '__main__':
    unittest.main()
