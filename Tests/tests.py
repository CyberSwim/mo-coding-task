import unittest
import shield_calc as sc

class TestMethods (unittest.TestCase):

    def test_data_import(self):
        self.assertEqual(sc.import_data(".\Tests\example1.txt"), ['2x3x4', '1x10x1', '5x7x4'])
        self.assertEqual(sc.import_data(), [""])
    
    def test_number_separator(self):
        self.assertEqual(sc.parse_numbers("1x2x3"), [1, 2, 3])
        self.assertEqual(sc.parse_numbers("99001x5031x3441"), [3441, 5031, 99001])

    def test_area_calc(self):
        self.assertEqual(sc.area_calc([5, 10, 20]), 700)
        self.assertEqual(sc.area_calc([2, 5, 3]), 62)

    def test_shield_contingency(self):
        self.assertEqual(sc.shield_contingency_calc([2, 6, 10]), 12)

    def test_wire_contingency(self):
        self.assertEqual(sc.wire_contingency_calc([2, 3, 8]), 10)

if __name__ == '__main__':
    unittest.main()
