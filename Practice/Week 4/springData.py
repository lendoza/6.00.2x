import pylab
import random


def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    discardHeader = dataFile.readline()
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)


def plotData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals * 9.81  # convert mass to force (F = mg)
    pylab.plot(xVals, yVals, 'bo', label='Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('Force (Newtons)')
    pylab.ylabel('Distance (Meters)')

# plotData('springData.txt')
# pylab.show()


def testErrors(ntrials=20000, npts=100):
    results = [0] * ntrials
    for i in xrange(ntrials):
        s = 0
        for j in xrange(npts):
            s += random.uniform(-1, 1)
        results[i] = s
    pylab.hist(results, bins=50)
    pylab.title('Sum of 100 random Points -- Triangular PDF(10,000 trials)')
    pylab.xlabel('Sum')
    pylab.ylabel('Number of trials')

testErrors()
pylab.show()
