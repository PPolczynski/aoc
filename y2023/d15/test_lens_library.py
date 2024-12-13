from unittest import TestCase

from y2023.d15.lenslibrary import LensLibrary


class LensLibraryTest(TestCase):
    def test_holiday_ascii_string_helper_algorithm(self):
        self.assertEqual(52, LensLibrary.holiday_ascii_string_helper_algorithm("HASH"))

    def test_get_hash_initialization_sequence(self):
        sequence = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
        self.assertEqual(1320, LensLibrary.get_hash_initialization_sequence(sequence))
