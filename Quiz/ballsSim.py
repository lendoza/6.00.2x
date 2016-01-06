import random


def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    score = 0
    tries = 0
    for n in xrange(numTrials):
        bucket = [0, 0, 0, 0, 1, 1, 1, 1]
        sum_ = 0
        for i in range(3):
            choice = random.choice(range(len(bucket)))
            sum_ += bucket[choice]
            del bucket[choice]
        if sum_ in (0, 3):
            score += 1
        tries += 1
    print float(score)/tries
