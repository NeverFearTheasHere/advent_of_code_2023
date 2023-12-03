import day03
import unittest

class Test_Day03(unittest.TestCase):
    def test_part1(self):
        exampleLines = [
            '467..114..' ,'...*......' ,'..35..633.' ,'......#...' ,'617*......' ,'.....+.58.' ,'..592.....' ,'......755.' ,'...$.*....' ,'.664.598..'
        ]
        self.assertEqual(day03.calculateSumOfPartNumbers(exampleLines), 4361)


if __name__ == '__main__':
    unittest.main()