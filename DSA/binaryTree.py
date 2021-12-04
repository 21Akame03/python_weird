class node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    # IMPORTANT left is smaller than parent and right greater
    def insert(self, data):
        if self.val:

            if data < self.val :
                # Check if theres a node in the left pos
                if self.left is None:
                    self.left = node(data)
                else:
                    # recursive: go deeper via the left node until a leaf node is found and instantiated
                    self.left.insert(data)

            elif data > self.val :
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)

        else:
            # if current node does not have any val
            self.val = data
    
    def print_node(self):
        if self.left:
            self.left.print_node()
        print(f"{self.val} -> ", end="")
        if self.right:
            self.right.print_node()

    # Left -> Root -> Right
    def inorder(self, root):
        treeList = []
        
        # if root exists go deep into left branch
        if root:
            treeList = self.inorder(root.left)
            treeList.append(root.val)
            treeList = treeList + self.inorder(root.right)

        return treeList
    
    # Root -> Left -> Right
    def preorder(self, root):
        treeList = []

        if root:
            treeList.append(root.val)
            treeList = treeList + self.preorder(root.left)
            treeList = treeList + self.preorder(root.right)

        return treeList

    # Left -> Right -> Root
    def postorder(self, root):
        treeList = []

        if root:
            treeList = self.postorder(root.left)
            treeList = treeList + self.postorder(root.right)
            treeList.append(root.val)
        
        return treeList

class BTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = node(data) 
            return False

        self.root.insert(data)

    def print_tree(self):
        if self.root:
            self.root.print_node()
    
    def inorder(self):
        if self.root:
            return self.root.inorder(self.root)
    
    def preorder(self):
        if self.root:
            return self.root.preorder(self.root)
    
    def postorder(self):
        if self.root:
            return self.root.postorder(self.root)

if __name__ == "__main__":
    B = BTree()
    B.insert(45)
    B.insert(89)
    B.insert(4)
    B.insert(20)
    B.insert(50)
    B.insert(860)

    B.print_tree()
    print("\n")

    # Modes of traversal 
    print(f"Inorder => {B.inorder()}")
    print(f"Preorder => {B.preorder()}")
    print(f"Postorder => {B.postorder()}")
