import random
import string
import time
import math

asciiStr = string.ascii_letters #both lower and upper case
lowerCaseLetters = 'abcdefghijklmnopqrstuvwxyz'

def test1():
    print(asciiStr[1] == 'b')

def infiniteMonkeType(inputStr):
    whitespaceCount = 0
    onlyLower = True
    for c in inputStr:
        if c == ' ':
            whitespaceCount += 1
        if c < 'a':
            onlyLower = False
    
    #choosing a character pool based on input string
    if (onlyLower):
        characterPool = lowerCaseLetters
    else:
        characterPool = asciiStr

    #Add an amount of whitespace to the character pool based on the rate of appearance in the input string
    characterPool += ' ' * math.ceil((whitespaceCount / len(inputStr)) * len(characterPool))

    inputLen = len(inputStr)
    attempts = 0
    i = 0
    monkeyStr = ""
    bestAttempt = 0
    attemptMilestone = 1

    while (i < inputLen):
        if (attempts == attemptMilestone):
            print("Attempt",attempts,"reached.")
            attemptMilestone *= 10

        c = random.choice(characterPool)
        
        if (c == inputStr[i]):
            monkeyStr += c
            i += 1
            if (len(monkeyStr) > bestAttempt):
                bestAttempt = len(monkeyStr)
                print("Attempt", attempts,",", monkeyStr)
        else:
            monkeyStr = ""
            attempts += 1
            i = 0
    
    return attempts
    
def formatFloat(num):
    return "{:.2f}".format(num)

def main():
    startTime = time.perf_counter()
    inputStr = input("Please enter the string you want the monkey to type (recommended less than 7 characters): ")
    sampleSize = int(input("Please enter how many times you want the monkey to try to type this string (recommended 10 or less as a start): "))
    attemptsTotal = 0

    for i in range(sampleSize):
        attemptsTotal += infiniteMonkeType(inputStr)
        
    endTime = time.perf_counter()
    timeDiff = endTime - startTime

    attemptsAverage = attemptsTotal / sampleSize

    print("Over", sampleSize, "attempts, the monkey took an average of", attemptsAverage, "attempts to type", "\"" + inputStr + "\"")
    print("The expected average number of attempts is:", math.pow(len(lowerCaseLetters), len(inputStr)))
    print("Total time:", formatFloat(timeDiff),", on average:", formatFloat(timeDiff/sampleSize))
    print("Attempts per second:", attemptsTotal/timeDiff)
    input()
    
main()