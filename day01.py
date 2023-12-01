def calculateCalibrationValue(inputLines):
    calibrationValueTotal = 0
    for line in inputLines:
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


if __name__ == "__main__":
    with open('day01_input.txt') as file:
        lines = file.read().splitlines()
        answer = calculateCalibrationValue(lines)
        print(answer)