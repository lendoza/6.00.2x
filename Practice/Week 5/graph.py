class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight=1.0):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src) +'->('\
            + str(self.weight) + ')'\
            + str(self.dest)


class Digraph(object):
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNodes(self, node):
        if node in self.nodes:
            reaise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []
    def addEdge(self,edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOF(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ""
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]


class Edge(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        reverse = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, reverse)


# Depth First Search

def DFS(graph, start, end, path=[]):
    path = path + [start]
    print 'Current dfs path', printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            newPath = DFS(graph, node, end, path)
            if newPath is not None:
                return newPath
    return None

# Shortest Path Depth First Search

def SPDFS(graph, start, end, path=[], shortest=None):
    path = path + [start]
    print 'Current dfs path', printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest = None or len(path) < len(shortest): # Keeps track of shortest path      
                newPath = DFS(graph, node, end, path, shortest)
                if newPath is not None:
                    shortest = newPath
    return shortest

# Bredth First Search

def BFS(graph, start, end, q=[]):
    initPath = [start]
    q.append(initPath)
    while len(q) != 0:
        tmpPath = q.pop(0)
        lastNode = tmpPath[len(tmpPath) - 1]
        print 'Current dequeued path:', printPath(tmpPath)
        if lastNode == end:
            return tmpPath
        for linkNode in graph.childrenOf(lastNode):
            if linkNode not in tmpPath:
                newPath = tmpPAth + [linkNode]
                q.append(newPath)
    return None
