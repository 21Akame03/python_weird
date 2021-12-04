class node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.nxt = nxt

class SLinkedList:
    def __init__(self):
        self.head = None

    def isHeadNUll(self) : 
        return not self.head

    def addHead(self, val) :
        if self.isHeadNUll():
            self.head = node(val)

            return None

        newNode = node(val, self.head)
        self.head = newNode
        
        print(f'added new head of val {val}')

    # Needs to be fixed
    def addTail(self, val) :
        if self.isHeadNUll():
            self.head = node(val)

            return None

        Node = self.head
        while Node.nxt:
            Node = Node.nxt

        Node.nxt = node(val)

        print(f'added new tail of val {val}')

    def printLinkedList(self):
        if self.isHeadNUll():
            print('No value in linked list')

            return None

        Node = self.head
        print()
        while Node.nxt:
            print (f'{Node.val} -> ', end="")
            Node = Node.nxt
        print(f'{Node.val}')

if __name__ == '__main__':
    linkedList = SLinkedList()

    linkedList.addHead(45)
    linkedList.addHead(4)
    linkedList.addHead(485)
    linkedList.addHead(45651)
    
    # Needs to be fixed
    linkedList.addTail(55)
    linkedList.addTail(5)
    linkedList.addTail(505)
    
    
    linkedList.printLinkedList()
