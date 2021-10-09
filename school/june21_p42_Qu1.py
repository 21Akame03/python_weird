class node:
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode


linkedlist = [node(1,1), node(5,4), node(6,7), node(7,-1), node(2, 2), node(0, 6), node(0,8), node(56,3), node(0,9), node(0,-1)]

# pointers
startPointer = 0
emptyList = 5


def outputNodes(linkedlist, startPointer):
    list = linkedlist
    currNode = list[startPointer]
    

    for i in range(len(list)):
        print(currNode.data)
        
        # check if its EOL or End Of List
        if currNode.nextNode == -1:
            break
        
        # change to the next node 
        currNode = list[currNode.nextNode]


def addNode(linkedList, startPointer, emptyList):
    val = input("Enter value to add to linked list : ")

    if emptyList < 0 or emptyList > 9:
        return 
    
    list = linkedList
    currNode = list[startPointer]

    while not currNode.nextNode == -1: 
        currNode = list[currNode.nextNode]
    
    # change the nextnode value to last index of the array + 1 
    currNode.nextNode = len(list)
    # add newnode to the array with nextnode of -1 for EOL
    linkedList.append(node(val, -1))
    
    # return list since primitive structures (primitive datatypes, list, dictionaries) values are passed by value
    return True



outputNodes(linkedlist, startPointer)
print()
addNode(linkedlist, startPointer, emptyList)
outputNodes(linkedlist, startPointer)

