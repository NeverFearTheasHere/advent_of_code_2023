import day01
import unittest

class Test_Day01(unittest.TestCase):
    def test_calculateCalibrationValue(self):
        exampleLines = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
        self.assertEqual(day01.calculateCalibrationValue(exampleLines), 142)

if __name__ == '__main__':
    unittest.main()