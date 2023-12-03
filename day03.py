import re


def calculateSumOfPartNumbers(engineSchematicLines):
    sumOfPartNumbers = 0
    numberOfLines = len(engineSchematicLines)
    lengthOfEachLine = len(engineSchematicLines[0]) # assuming all lines in the schematic are the same length

    for index, line in enumerate(engineSchematicLines):
        candidatePartNumbers = re.finditer('\d+', line)
        for candidatePartNumber in candidatePartNumbers:
            (startIndex, endIndex) = candidatePartNumber.span()
            adjacentCharactersOnCurrentLine = line[max(startIndex - 1, 0):min(endIndex + 1, lengthOfEachLine)]
            adjacentCharactersOnPreviousLine = ''
            adjacentCharactersOnNextLine = ''
            if index > 0:
                previousLine = engineSchematicLines[index - 1]
                adjacentCharactersOnPreviousLine = previousLine[max(startIndex - 1, 0):min(endIndex + 1, lengthOfEachLine)]
            
            if index < numberOfLines - 1:
                nextLine = engineSchematicLines[index + 1]
                adjacentCharactersOnNextLine = nextLine[max(startIndex - 1, 0):min(endIndex + 1, lengthOfEachLine)]
            
            isPartNumber = re.search('[^\d|.]', adjacentCharactersOnPreviousLine + adjacentCharactersOnCurrentLine  + adjacentCharactersOnNextLine)

            if isPartNumber:
                sumOfPartNumbers += int(candidatePartNumber.group())

    return sumOfPartNumbers


def calculateSumOfGearRatios(engineSchematicLines):
    sumOfGearRatios = 0
    numberOfLines = len(engineSchematicLines)

    for index, line in enumerate(engineSchematicLines):
        candidateGears = re.finditer('\*', line)
        for candidateGear in candidateGears:
            numbersAdjacentToGear = []
            gearIndex = candidateGear.start()

            if index > 0:
                previousLine = engineSchematicLines[index - 1]
                numberMatchesOnPreviousLine = re.finditer('\d+', previousLine)
                for numberMatch in numberMatchesOnPreviousLine:
                    if numberMatch.start() - 1 <= gearIndex and gearIndex <= numberMatch.end():
                        numbersAdjacentToGear.append(numberMatch.group())

            numberMatchesOnCurrentLine = re.finditer('\d+', line)
            for numberMatch in numberMatchesOnCurrentLine:
                if numberMatch.start() - 1 <= gearIndex and gearIndex <= numberMatch.end():
                    numbersAdjacentToGear.append(numberMatch.group())

            if index < numberOfLines - 1:
                nextLine = engineSchematicLines[index + 1]
                numberMatchesOnNextLine = re.finditer('\d+', nextLine)
                for numberMatch in numberMatchesOnNextLine:
                    if numberMatch.start() - 1 <= gearIndex and gearIndex <= numberMatch.end():
                        numbersAdjacentToGear.append(numberMatch.group())

            isGear = len(numbersAdjacentToGear) > 1

            if isGear:
                gearRatio = 1
                for number in numbersAdjacentToGear:
                    gearRatio = gearRatio * int(number)
                sumOfGearRatios += gearRatio

    return sumOfGearRatios


if __name__ == "__main__":
    with open('day03_input.txt') as engineSchematicFile:
        engineSchematicLines = engineSchematicFile.read().splitlines()
        answer = calculateSumOfGearRatios(engineSchematicLines)
        print(answer)