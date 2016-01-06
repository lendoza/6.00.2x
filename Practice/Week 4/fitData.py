import pylab


def getData(fileName):
    dataFile = open('springData.txt', 'r')
    distances = []
    masses = []
    discardHeader = dataFile.readline()
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)

# Hookes Law

def fitData(filename):
    xVals, yVals = getData('fileName')
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals * 9.81  # convert mass to force (f = mg)
    pylab.plot(xVals, yVals, 'bo', label='Measure points')
    pylab.xlabel('Measured Displacement of Spring')
    pylab.ylabel('Force (Newtons)')
    pylab.ylabel('Distance (Meters)')
    a, b = pylab.polyfit(xVals, yVals, 1)  # fit y = ax + b
    estYVals = a*xVals + b
    k = 1/a
    pylab.plot(xVals, estYVals, label='Linear fit, k = ' + str(round(k, 5)))
    pylab.legend(loc='best')


# fitData('springData.txt')
# pylab.show()

# Termans Law

def fitData1(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals * 9.81 # convert mass to force (f = mg)
    pylab.plot(xVals, yVals, 'bo', label='Measured Points')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('Force (Newtons)')
    pylab.ylabel('Distance (Meters)')
    a, b = pylab.polyfit(xVals, yVals, 1) # fit y = ax + b
    estYVals = a*xVals + b
    pylab.plot(xVals, estYVals, label='Linear fit')
    a, b, c, d = pylab.polyfit(xVals, yVals, 3)
    estYVals = a*(xVals**3) + b*xVals**2 + c*xVals + d
    pylab.plot(xVals, estYVals, label='Cubic Fit')
    pylab.legend(loc='best')

fitData1('springData.txt')
pylab.show()
