class Cluster(object):
    """ A Cluster is defines as a set of elements, all having 
    a particular type """
    def __init__(self, points, pointType):
        """ Elements of a cluster are saved in self.points
        and the pointType is also saved """
        self.points = points
        self.pointType = pointType
    def singleLinkageDist(self, other):
        """ Returns the float distance between the points that 
        are closest to each other, where one point is from 
        self and the other point is from other. Uses the 
        Euclidean dist between 2 points, defined in Point."""
        minDist = None
        for point1 in self.points:
            for point2 in other.members():
                if minDist == None:
                    minDist = point1.distance(point2)
                minDist = min(minDist, point1.distance(point2))
        return minDist

    def maxLinkageDist(self, other):
        """ Returns the float distance between the points that 
        are farthest from each other, where one point is from 
        self and the other point is from other. Uses the 
        Euclidean dist between 2 points, defined in Point."""
        maxDist = 0
        for point1 in self.points:
            for point2 in other.members():
                maxDist = max(maxDist, point1.distance(point2))
        return maxDist

    def averageLinkageDist(self, other):
        """ Returns the float average (mean) distance between all 
        pairs of points, where one point is from self and the 
        other point is from other. Uses the Euclidean dist 
        between 2 points, defined in Point."""
        totalDist = 0
        numPairs = 0
        for point1 in self.points:
            for point2 in other.members():
                totalDist += point1.distance(point2)
                numPairs +=1
        return totalDist/numPairs

    def mysteryLinkageDist(self, other):
        av_dist = self.averageLinkageDist(other)
        max_dist = self.maxLinkageDist(other)
        min_dist = self.singleLinkageDist(other)
        retDist = 0.0
        if av_dist == max_dist and max_dist == min_dist:
            retDist = av_dist
        elif av_dist == max_dist:
            retDist = av_dist
        elif av_dist == min_dist:
            retDist = av_dist
        elif max_dist == min_dist:
            retDist = min_dist
        else:
            retDist = random.choice([av_dist,min_dist,max_dist])
        return retDist

    def members(self):
        for p in self.points:
            yield p
    def isIn(self, name):
        """ Returns True is the element named name is in the cluster
        and False otherwise """
        for p in self.points:
            if p.getName() == name:
                return True
        return False
    def toStr(self):
        result = ''
        for p in self.points:
            result = result + p.toStr() + ', '
        return result[:-2]
    def getNames(self):
        """ For consistency, returns a sorted list of all 
        elements in the cluster """
        names = []
        for p in self.points:
            names.append(p.getName())
        return sorted(names)
    def __str__(self):
        names = self.getNames()
        result = ''
        for p in names:
            result = result + p + ', '
        return result[:-2]

mysteryLinkageDist()
