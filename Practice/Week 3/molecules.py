import pylab
import random

# Exponential Distribution

def clear(n, clearProb, steps):
	numRemaining = [n]
	for t in range(steps):
		numRemaining.append(n * (1 - clearProb)**t)
	pylab.plot(numRemaining, label='Exponential Decay')

# Monte Carlo Simulation

def clearSim(n, clearProb, steps):
	numRemaining = [n]
	for t in range(steps):
		numLeft = numRemaining[-1]
		for m in range(numRemaining[-1]):
			if random.random() <= clearProb:
				numLeft -= 1
		numRemaining.append(numLeft)
	pylab.plot(numRemaining, 'ro', label='Simulation')


clear(1000, 0.1, 500)
clearSim(100, 0.1, 500)
pylab.xlabel("Number of Steps")
pylab.ylabel("Number of Molecules")
pylab.title("Clearance of Molecules")
pylab.show()
