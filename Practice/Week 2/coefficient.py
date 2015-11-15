def stdDev(X):
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5


def CV(X):
	mean = sum(X) / float(len(X))
	try:
		return stdDev(X)/mean
	except ZeroDivisionError:
		return float('NaN')

print CV([10, 4, 12, 15, 20, 5])
