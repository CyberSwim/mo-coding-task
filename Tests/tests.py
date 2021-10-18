import unittest
import wire_shield_calc as wsc

class TestMethods (unittest.TestCase):
    """Unit tests for each function in `wire_shield_calc.py`.
    
    """
    
    # Tests the `import_data` function
    def test_data_import(self):
        self.assertEqual(wsc.import_data(".\Tests\example1.txt"), ['2x3x4', '1x10x1', '5x7x4'])
        self.assertEqual(wsc.import_data(""), ['']) # tests function with no parameters

        # tests incorrect path handling
        self.assertEqual(wsc.import_data("C:\Fake Path"), [''])
    
    # Tests the `parse_numbers` function
    def test_number_separator(self):
        self.assertEqual(wsc.parse_numbers("1x2x3"), [1, 2, 3])
        self.assertEqual(wsc.parse_numbers("99001x5031x3441"), [3441, 5031, 99001])

    # Tests the `area_calc` function
    def test_area_calc(self):
        self.assertEqual(wsc.area_calc([4, 6, 6], "shield"), 192)
        self.assertEqual(wsc.area_calc([2, 2, 5], "wire"), 28)


class TestProgram (unittest.TestCase):
    """Tests the full program `wire_shield_calc.py` against three example data sets.
    
    """

    def test_examples(self):
        self.assertEqual(wsc.calculate_result(".\Tests\example1.txt"), (287, 206))
        self.assertEqual(wsc.calculate_result(".\Tests\example2.txt"), (6024, 12520))
        self.assertEqual(wsc.calculate_result(".\Tests\example3.txt"), (73889, 183524))


if __name__ == '__main__':
    unittest.main()