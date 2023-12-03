import day01
import unittest

class Test_Day01(unittest.TestCase):
    def test_part1(self):
        exampleLines = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
        self.assertEqual(day01.calculateCalibrationValue(exampleLines), 142)

    def test_part2(self):
        exampleLines = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']
        self.assertEqual(day01.calculateCalibrationValue(exampleLines), 281)

if __name__ == '__main__':
    unittest.main()