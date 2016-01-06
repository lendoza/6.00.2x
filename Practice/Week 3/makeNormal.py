import random
import pylab


def makeNormal(mean, sd, numSamples):
	samples = []
	for i in range(numSamples):
		samples.append(random.gauss(mean, sd))
	pylab.hist(samples, bins=101)

makeNormal(0.0, 1.0, 10000)
pylab.show()
