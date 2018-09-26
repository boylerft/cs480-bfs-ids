import time
from collections import deque

size = 5
maxStack = 1

class Node:
    def __init__(self):
        self.__permutation = None
        self.__parent = None
    def fill(self, permutation, parent):
        self.__permutation = permutation
        self.__parent = parent
    def getPerm(self):
        return self.__permutation
    def getParent(self):
        return self.__parent
        

def bfs(permutation, n):
    maxSize = 1
    
    pointers = []
    myQueue = deque()
    myStack = deque()
    #currentPerm
    # fix
    node = Node()
    node.fill(permutation, -1)
    
    cpu0 = time.clock()
    pointers.append(node)
    myQueue.append(node)
  #  print(len(myQueue))
    while (len(myQueue) != 0):
      #  print("while loop")
        '''
        if (len(myQueue) >= maxSize):
        #    print("if statement")
            maxSize = len(myQueue)
            node = myQueue[0]
            myQueue.popleft()
        '''
        if (generateChilds(node, pointers, myQueue, myStack, 1)):
              #  int cpu1 = time.clock()
            printPath(pointers)
            print("Total cpu time for bfs: ", time.clock(), " seconds")
            print("Total number of visited states: ", len(pointers))
            print("Max size of Queue", len(myQueue))
            return 
               
def dfs (node, n, pointers):
    if (n == 0):
        return False
    myStack = deque()
    myQueue = deque()
    pointers.append(node)
    myStack.append(node)
    maxStack = 1
    node = myStack[len(myStack)-1]
    myStack.popleft()
    
    if (generateChilds(node, pointers, myQueue, myStack, 0)):
        return True
    if (maxStack < len(myStack)):
        maxStack = len(myStack)
    for i in range (0, len(myStack)):
        node = myStack[len(myStack)-1]
        myStack.popleft()
        if (dfs(node, n-1, pointers)):
            return True
    return False

def ids (permutation, maxDepth):
    cpu0 = time.clock()
    for i in range(0, maxDepth):
        pointers = []
        node = Node()
        node.fill(permutation, -1)
        pointers.append(node)
        if (dfs(node, i, pointers)):
            printPath(pointers)
            print("Total cpu time for ids: ", time.clock(), " seconds")
            print("Total number of visited states: ", len(pointers))
            print("Max size of Queue: ", maxStack)
            return
    print("Could not find.. max depth should increase")
    
                
def generateChilds(node, pointers, myQueue, myStack, ch):
#    print("at generate child ")
    #find(pointers.begin, pointers.end, node) - pointers.begin
   # print(pointers[0])
   # if node in pointers:
    parentIdx = pointers.index(node) #- pointers.index(pointers[]
        #print(parentIdx)                                             
    perm = node.getPerm()
    
    for i in range(1, size):
     #   print("i: ", i)
        for j in range(0, size):
      #      print("j:", j)
          #  print("for loop")
            if ((j + i) > size - 1):
                break
            newPerm = flip(perm, i + j, j)
            intVal = 0 
            oldVal = 1
            
            if (intVal != oldVal):
                leaf = Node()
                leaf.fill(newPerm, parentIdx)
                pointers.append(leaf)
                # inorder
                if (inOrder(newPerm)):
                    return True
                
                if (ch == 1):
                    myQueue.appendleft(leaf)
                else:
                    myStack.appendleft(leaf)
                    
    return False

def flip (permutation, endIdx, startingIdx):
   # int tempArr = (int *)malloc(sizeof(int) * size )
    tempArr = []
  #  for i in range(0, size):
    tempArr = permutation.copy()
    
    tempVal = 0
    while(startingIdx < endIdx):
        tempVal = tempArr[startingIdx]
        tempArr[startingIdx] = tempArr[endIdx]
        tempArr[endIdx] = tempVal
        endIdx -= 1
        startingIdx += 1
        
    return tempArr

def inOrder(arr):
    for i in range(0, size-1):
        if(arr[i] > arr[i + 1]):
            return False
    return True

def printArray(arr):
    for i in range(0, size):
        print(arr[i], ",")

def printPath(pointers):
    vals = []
    node = pointers[len(pointers) - 1]
    cond = node.getParent()
    print("cond: ", cond)
    while (cond != -1):
        i = 0
        print("perm 106", i, node.getPerm())
        i += 1
        vals_app = node.getPerm()
        vals.append(vals_app)
        node_parent = node.getParent()
        node = node_parent in pointers
        
    vals.append(node.getPerm())
   # for i in range(len(vals) - 1, -1):
    i = len(vals) - 1
    while(i > -1):
        i = len(vals) - 1
        printArray(vals[i])
        print("->")
        i -= 1
    print("")

    
    
def main():
    vals = [5,2,4,3,1]
  #  print("Enter Values you would like to test: ")
    '''
    userInput = int(input("Enter values: "))
    t = []
    t = int(i) for i in userInput.split():
    for i in userInput.split():
        t.append(i)
    t.split()
    print(t)
    '''
  #  for i in userInput.split():
   #     t.append(i) 
    print("Running bfs..")
  #  bfs(vals, 5)
#    print("Running ids..")
    ids(vals, 5)
    
main()