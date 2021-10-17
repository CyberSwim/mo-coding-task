import unittest
import wire_shield_calc as wsc

class TestMethods (unittest.TestCase):

    def test_data_import(self):
        self.assertEqual(wsc.import_data(".\Tests\example1.txt"), ['2x3x4', '1x10x1', '5x7x4'])
        self.assertEqual(wsc.import_data(), [""])
        
        with self.assertRaises(FileNotFoundError): wsc.import_data("C:\Fake Path")
    
    def test_number_separator(self):
        self.assertEqual(wsc.parse_numbers("1x2x3"), [1, 2, 3])
        self.assertEqual(wsc.parse_numbers("99001x5031x3441"), [3441, 5031, 99001])

    def test_area_calc(self):
        self.assertEqual(wsc.area_calc([5, 10, 20]), 700)
        self.assertEqual(wsc.area_calc([2, 5, 3]), 62)

    def test_shield_contingency(self):
        self.assertEqual(wsc.shield_contingency_calc([2, 6, 10]), 12)

    def test_wire_contingency(self):
        self.assertEqual(wsc.wire_contingency_calc([2, 3, 8]), 10)

if __name__ == '__main__':
    unittest.main()
