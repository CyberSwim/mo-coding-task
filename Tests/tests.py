import unittest
import shield_calc as sc

class TestMethods (unittest.TestCase):

    def test_data_import(self):
        self.assertEqual(sc.import_data(".\Tests\example1.txt"), ['2x3x4', '1x10x1', '5x7x4'])
    
    def test_number_separator(self):
        self.assertEqual(sc.parse_numbers("1x2x3"), [1, 2, 3])
        self.assertEqual(sc.parse_numbers("3441x5031x99001"), [3441, 5031, 99001])

    def test_area_calc(self):
        self.assertEqual(sc.area_calc([2, 5, 3]), 62)

    def test_shield_contingency(self):
        self.assertEqual(sc.shield_contingency_calc([10, 6, 2]), 12)

    def test_wire_contingency(self):
        self.assertEqual(sc.wire_contingency_calc([2, 8, 3]), 10)

if __name__ == '__main__':
    unittest.main()