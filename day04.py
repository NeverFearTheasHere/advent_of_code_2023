import re


def calculateTotalScratchcardPoints(scratchcardInputs):
    totalScratchcardPoints = 0

    for scratchcard in scratchcardInputs:
        numbersSections = scratchcard.split(': ')[1]
        [winningNumbersSection, myNumbersSection] = numbersSections.split('| ')
        winningNumbers = [int(x) for x in re.findall(r'\d+', winningNumbersSection)]
        myNumbers = [int(x) for x in re.findall(r'\d+', myNumbersSection)]

        scratchcardScore = 0
        for winningNumber in winningNumbers:
            if winningNumber in myNumbers:
                if scratchcardScore == 0:
                    scratchcardScore = 1
                else:
                    scratchcardScore = scratchcardScore * 2

        totalScratchcardPoints += scratchcardScore

    return totalScratchcardPoints


def calculateNumberOfScratchcards(scratchcardInputs):
    countOfscratchcardsCopiesByCardNumber = { }

    for scratchcard in scratchcardInputs:
        [cardLabel, numbersSections] = scratchcard.split(r': ')
        cardNumber = int(re.search(r'\d+', cardLabel).group())
        [winningNumbersSection, myNumbersSection] = numbersSections.split(r'| ')
        winningNumbers = [int(x) for x in re.findall(r'\d+', winningNumbersSection)]
        myNumbers = [int(x) for x in re.findall(r'\d+', myNumbersSection)]
        
        additionalCardNumber = cardNumber
        for winningNumber in winningNumbers:
            if winningNumber in myNumbers:
                additionalCardNumber = additionalCardNumber + 1
                if additionalCardNumber in countOfscratchcardsCopiesByCardNumber:
                    countOfscratchcardsCopiesByCardNumber[additionalCardNumber] += countOfscratchcardsCopiesByCardNumber[cardNumber] + 1
                else:
                    if cardNumber in countOfscratchcardsCopiesByCardNumber:
                        countOfscratchcardsCopiesByCardNumber[additionalCardNumber] = countOfscratchcardsCopiesByCardNumber[cardNumber] + 1
                    else:
                        countOfscratchcardsCopiesByCardNumber[additionalCardNumber] = 1
    
    numberOfCopies = sum(countOfscratchcardsCopiesByCardNumber.values())
    return len(scratchcardInputs) + numberOfCopies


if __name__ == "__main__":
    with open('day04_input.txt') as scratchcardFile:
        scratchcardInputs = scratchcardFile.read().splitlines()
        answer = calculateNumberOfScratchcards(scratchcardInputs)
        print(answer)