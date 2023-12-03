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

if __name__ == "__main__":
    with open('day03_input.txt') as engineSchematicFile:
        engineSchematicLines = engineSchematicFile.read().splitlines()
        answer = calculateSumOfPartNumbers(engineSchematicLines)
        print(answer)