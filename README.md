# Infinite Monke Simulator

## Introduction:

The Infinite Monkey Theorem is as follows:

"The infinite monkey theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type any given text" - taken from wikipedia (https://en.wikipedia.org/wiki/Infinite_monkey_theorem)

This console app is a simple implementation of the infinite typing monkey, which will take an input string and attempt to type out that string, and provide some analysis of runtime and number of attempts taken at the end.

Demo screenshot:

![infinite monkey](https://github.com/user-attachments/assets/2df80320-ac49-4eed-91a0-14f81452870c)


We must imagine the monke happy.

## Features:
### Input Analysis:
By default, the pool of characters to choose from is only 26 lowercase characters.

The monkey will analyze the input string to check if there are uppercase characters and whitespace, then add the set of uppercase letters and whitespace to the character pool as needed.

### Attempts count and runtime analyses:
The monkey will keep track of the number of attempts taken each time it tries to successfully replicate the input string.

The monkey will keep track of how much time it took and report the total and average time taken for all attempts, along with number of attempts it could do per second (to account for different computers' performance).

## The Math:
Assuming a lowercase word, the chance of typing out a word of n length should be 1/((1/26) ^ n).

Example: a word of length 5 should take about 1 / ((1/26)^5) = 11881376 attempts on average.
The program confirms this prediction for this simple case.

## Optimization:
Instead of guessing the entire string every attempt, the monkey types one letter at a time and only continue guessing the next letter if it guesses one letter correctly.

Doing this seems to have decreased time taken by 66-75%. Nice to have but still the same time complexity.

## Conclusione
The monkey is practically performing a bruteforce attack to guess the input string. At this stage, it is nothing more than a funny thought experiment and a waste of computing resource.

## Quickstart Guide
Double-click the file named "InfiniteMonkeSimulator.py", patiently observe.
