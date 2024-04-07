import random
import string
import time

asciiStr = string.ascii_letters
lowerCaseLetters = 'abcdefghijklmnopqrstuvwxyz'

def test1():
    print(asciiStr[1] == 'b')

def infiniteMonkeyType(inputStr, characterPool):
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
    inputStr = "asia"
    attemptsTotal = 0
    sampleSize = 100

    for i in range(sampleSize):
        attemptsTotal += infiniteMonkeyType(inputStr, lowerCaseLetters)
    endTime = time.perf_counter()
    timeDiff = endTime - startTime

    attemptsAverage = attemptsTotal / sampleSize

    print("Over", sampleSize, "attempts, the monkey took and average of", attemptsAverage, "attempts to type", inputStr)
    print("Total time:", formatFloat(timeDiff),", on average:", formatFloat(timeDiff/sampleSize))
    print("Attempts per second:", attemptsTotal/timeDiff)

main()