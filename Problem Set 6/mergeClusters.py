class ClusterSet(object):
    """ A ClusterSet is defined as a list of clusters """
    def __init__(self, pointType):
        """ Initialize an empty set, without any clusters """
        self.members = []
    def add(self, c):
        """ Append a cluster to the end of the cluster list
        only if it doesn't already exist. If it is already in the 
        cluster set, raise a ValueError """
        if c in self.members:
            raise ValueError
        self.members.append(c)
    def getClusters(self):
        return self.members[:]
    def mergeClusters(self, c1, c2):
        """ Assumes clusters c1 and c2 are in self
        Adds to self a cluster containing the union of c1 and c2
        and removes c1 and c2 from self """
        mergedPoints = list(c1.members()) + list(c2.members())
        mergedCluster = Cluster(mergedPoints, type(mergedPoints[0]))
        self.members.remove(c1)
        self.members.remove(c2)
        self.add(mergedCluster)

    def findClosest(self, linkage):
        """ Returns a tuple containing the two most similar 
        clusters in self
        Closest defined using the metric linkage """
        minDist = None
        result = ()
        for i, cluster1 in enumerate(self.members):
            for cluster2 in self.members[i+1:]:
                if minDist == None:
                    minDist = linkage(cluster1,cluster2)
                    result = (cluster1,cluster2)
                else:
                    currentDistance = linkage(cluster1,cluster2)
                    if currentDistance < minDist:
                        minDist = currentDistance
                        result = (cluster1, cluster2)
        return result

    def mergeOne(self, linkage):
        """ Merges the two most simililar clusters in self
        Similar defined using the metric linkage
        Returns the clusters that were merged """
        clustersToMerge = self.findClosest(linkage)
        self.mergeClusters(clustersToMerge[0],clustersToMerge[1])
        return clustersToMerge

    def numClusters(self):
        return len(self.members)
    def toStr(self):
        cNames = []
        for c in self.members:
            cNames.append(c.getNames())
        cNames.sort()
        result = ''
        for i in range(len(cNames)):
            names = ''
            for n in cNames[i]:
                names += n + ', '
            names = names[:-2]
            result += '  C' + str(i) + ':' + names + '\n'
        return result
