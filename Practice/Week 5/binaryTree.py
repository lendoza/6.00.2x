class binaryTree(object):
    def __init__(self, value):
        self.value = value
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None
    def setLeftBranch(self, node):
        self.leftBranch = node
    def setRightBranch(self, node):
        self.rightBranch = node
    def setParent(self, parent):
        self.parent = parent
    def getValue(self):
        return self.value
    def getLeftBranch(self):
        return self.leftBranch
    def getRightBranch(self):
        return self.rightBranch
    def getParent(self):
        return self.parent
    def __str__(self):
        return self.value

# Depth First Search

def DFSBinary(root, fcn):
    stack = [root]
    while len(stack) > 0:
        if fcn(stack[0]):
            return True
        else:
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
    return False

# Bredth First Search

def BFSBinary(root, fcn):
    queue = [root]
    while len(queue) > 0:
        if fcn(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            if temp.getRightBranch():
                queue.append(0, temp.getRightBranch())
            if temp.getLeftBranch():
                queue.append(0, temp.getLeftBranch())
    return False

# Depth First Ordered Search

def DFSBinaryOrdered(root, fcn, ltFcn):
    stack = [root]
    while len(stack) > 0:
        if fcn(stack[0]):
            return True
        elif ltFcn(stack[0]):
            temp = stack.pop(0)
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
        else:
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
    return False


def buildDTree(sofar, todo):
    if len(todo) == 0:
        return binaryTree(sofar)
    else:
        withelt = buildDTree(sofar + [todo[0]], todo[1:])
        withoutelt = buildDTree(sofar, todo[1:])
        here = binaryTree(sofar)
        here.setLeftBranch(withelt)
        here.setRightBranch(withoutelt)
        return here

# Depth First Search - Decision Tree

def DFSDTree(root, valueFcn, constraintFcn):
    stack = [root]
    best = None
    visited = 0
    while len(stack) > 0:
        visited += 1
        if constraintFcn(stack[0].getValue()):
            if best is None:
                best = stack[0]
            elif valueFcn(stack[0].getValue()) > valueFcn(best.getValue()):
                best = stack[0]
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
        else:
            stack.pop(0)
    print 'visited', visited
    return best

# Bredth First Search - Decision Tree

def DFSDTree(root, valueFcn, constraintFcn):
    queue = [root]
    best = None
    visited = 0
    while len(queue) > 0:
        visited += 1
        if constraintFcn(queue[0].getValue()):
            if best is None:
                best = queue[0]
            elif valueFcn(queue[0].getValue()) > valueFcn(best.getValue()):
                best = queue[0]
            temp = queue.pop(0)
            if temp.getLeftBranch():
                queue.append(temp.getLeftBranch())
            if temp.getRightBranch():
                queue.append(temp.getRightBranch())
        else:
            queue.pop(0)
    print 'visited', visited
    return best
