import re


def calculateSumOfPossibleGameIds(inputLines):
    sumOfPossibleGameIds = 0
    for line in inputLines:
        gameId = int(re.search('\d+', line).group())

        if gameIsPossible(line):
            sumOfPossibleGameIds += gameId

    return sumOfPossibleGameIds


def gameIsPossible(line):
    # check if this game is possible if there are 12 red cubes, 13 green cubes, and 14 blue cubes
    maxNumberOfRedCubes = max([int(x) for x in re.findall('\d+(?= red)', line)])
    maxNumberOfGreenCubes = max([int(x) for x in re.findall('\d+(?= green)', line)])
    maxNumberOfBlueCubes = max([int(x) for x in re.findall('\d+(?= blue)', line)])
    return maxNumberOfRedCubes <= 12 and maxNumberOfGreenCubes <= 13 and maxNumberOfBlueCubes <= 14


def calculateTotalPowerOfMinimumSetOfCubes(inputLines):
    sumOfPowersOfMinimumSetsOfCubes = 0
    for line in inputLines:
        sumOfPowersOfMinimumSetsOfCubes += calculatePowerOfMinimumSetOfCubes(line)

    return sumOfPowersOfMinimumSetsOfCubes


def calculatePowerOfMinimumSetOfCubes(line):
    # The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together
    maxNumberOfRedCubes = max([int(x) for x in re.findall('\d+(?= red)', line)])
    maxNumberOfGreenCubes = max([int(x) for x in re.findall('\d+(?= green)', line)])
    maxNumberOfBlueCubes = max([int(x) for x in re.findall('\d+(?= blue)', line)])
    return maxNumberOfRedCubes * maxNumberOfGreenCubes * maxNumberOfBlueCubes


if __name__ == "__main__":
    with open('day02_input.txt') as file:
        lines = file.read().splitlines()
        answer = calculateTotalPowerOfMinimumSetOfCubes(lines)
        print(answer)