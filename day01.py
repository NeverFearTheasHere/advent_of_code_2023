def calculateCalibrationValue(inputLines):
    calibrationValueTotal = 0
    for line in inputLines:
        line = replaceSpelledOutDigits(line)
        calibrationValueFirstDigit = ''
        calibrationValueSecondDigit = ''
        for character in line:
            if character in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if calibrationValueFirstDigit == '':
                    calibrationValueFirstDigit = character
                calibrationValueSecondDigit = character
        calibrationValue = int(calibrationValueFirstDigit + calibrationValueSecondDigit)
        calibrationValueTotal += calibrationValue

    return calibrationValueTotal

def replaceSpelledOutDigits(inputString):
    inputString = inputString.replace('one', 'one1one')
    inputString = inputString.replace('two', 'two2two')
    inputString = inputString.replace('three', 'three3three')
    inputString = inputString.replace('four', 'four4four')
    inputString = inputString.replace('five', 'five5five')
    inputString = inputString.replace('six', 'six6six')
    inputString = inputString.replace('seven', 'seven7seven')
    inputString = inputString.replace('eight', 'eight8eight')
    inputString = inputString.replace('nine', 'nine9nine')
    return inputString

if __name__ == "__main__":
    with open('day01_input.txt') as file:
        lines = file.read().splitlines()
        answer = calculateCalibrationValue(lines)
        print(answer)