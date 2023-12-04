import re


def calculateTotalScratchcardPoints(scratchcardInputs):
    totalScratchcardPoints = 0

    for scratchcard in scratchcardInputs:
        numbersSections = scratchcard.split(': ')[1]
        [winningNumbersSection, myNumbersSection] = numbersSections.split('| ')
        winningNumbers = [int(x) for x in re.findall('\d+', winningNumbersSection)]
        myNumbers = [int(x) for x in re.findall('\d+', myNumbersSection)]

        scratchcardScore = 0
        for winningNumber in winningNumbers:
            if winningNumber in myNumbers:
                if scratchcardScore == 0:
                    scratchcardScore = 1
                else:
                    scratchcardScore = scratchcardScore * 2

        totalScratchcardPoints += scratchcardScore

    return totalScratchcardPoints


if __name__ == "__main__":
    with open('day04_input.txt') as scratchcardFile:
        scratchcardInputs = scratchcardFile.read().splitlines()
        answer = calculateTotalScratchcardPoints(scratchcardInputs)
        print(answer)