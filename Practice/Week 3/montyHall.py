import random
import pylab


def montyChoose(guessDoor, prizeDoor):
    if 1 != guessDoor and 1 != prizeDoor:
        return 1
    if 2 != guessDoor and 2 != prizeDoor:
        return 2
    return 3


def randomChoose(guessDoor, prizeDoor):
    if guessDoor == 1:
        return random.choice([2, 3])
    if guessDoor == 2:
        return random.choice([1, 3])
    return random.choice([1, 2])


def simMontyHall(chooseFcn, numTrials=100):
    stickWins, switchWins, noWin = (0, 0, 0)
    prizeDoor = [1, 2, 3]
    guess = [1, 2, 3]
    for t in range(numTrials):
        prizeDoor = random.choice([1, 2, 3])
        guess = random.choice([1, 2, 3])
        toOpen = chooseFcn(guess, prizeDoor)
        if toOpen == prizeDoor:
            noWin += 1
        elif guess == prizeDoor:
            stickWins += 1
        else:
            switchWins += 1
    return (stickWins, switchWins)


def displayMHSim(simResults, title):
    stickyWins, switchWins = simResults
    pylab.pie([stickWins, switchWins],
              colors=['r', 'c'],
              labels=['stick', 'change'],
              autopct=('%.2f%%')
