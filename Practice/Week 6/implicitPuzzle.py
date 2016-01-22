class puzzle (object):
    def __init__(self, order):
        self.label = order
        for index in range(9):
            if order[index] == '0':
                self.spot = index
                return None
    def transition(self, to):
        label = self.label
        blankLocation = self.spot
        newBlankLabel = str(label[to])
        newLabel = " "
        for i in range(9):
            if i == to:
                newLabel += "0"
            elif i == blankLocation:
                newLabel += newBlankLabel
            else:
                newLabel += str(label[i])
        return puzzle(newLabel)
    def __str__(self):
        return self.label

def BFSWithGenerator(start, end, q=[]):  # 220 moves
    initPath = [start]
    q.append(initPath)
    while len(q) != 0:
        tmpPath = q.pop(0)
        lastNode = tmpPath[len(tmpPath) - 1]
        if lastNode.label == end.label:
            return tmpPath
        for shift in shiftDict[lastNode.spot]:
            new = lastNode.transition(shift)
            if notInPath(new, tmpPath):
                newPath = tmpPath + [new]
                q.append(newPath)
    return None

def DFSWithGenerator(start, end, stack=[]):  # not efficient
    initPath = [start]
    stack.insert(0, initPath)
    while len(stack) != 0:
        tmpPath = stack.pop(0)
        lastNode = tmpPath[len(tmpPath) - 1]
        if lastNode.label == end.label:
            return tmpPath
        for shift in shiftDict[lastNode.spot]:
            new = lastNode.transition(shift)
            if notInPath(new, tmpPath):  # avoid cycles
                newPath = tmpPath + [new]
                stack.insert(0, newPath)
    return None


def notInPath(node, path):
    for elt in path:
        if node.label == elt.label:
            return False
    return True

shiftDict = {}
shiftDict[0] = [1, 3]
shiftDict[1] = [0, 2, 4]
shiftDict[2] = [1, 5]
shiftDict[3] = [0, 4, 6]
shiftDict[4] = [1, 3, 5, 7]
shiftDict[5] = [2, 4, 8]
shiftDict[6] = [3, 7]
shiftDict[7] = [4, 6, 8]
shiftDict[8] = [5, 7]

goal = puzzle('012345678')
test1 = puzzle('125638047')
path = BFSWithGenerator(test1, goal)

def printGrid(puzzle):
    data = puzzle.label
    print data[0], data[1], data[2]
    print data[3], data[4], data[5]
    print data[6], data[7], data[8]
    print " "

def printSolution(path):
    for elt in path:
        printGrid(elt)

print printSolution(path)
