class Node: 
    def __init__(self, val): 
        self.value = val 
        self.left = None
        self.right = None
        self.height = 1
  
  
class AVL_Tree: 
    def __init__(self) -> None:
        self.root: Node = None
    
    def add(self, value): 
        def wrapper(parent):
            if not parent: 
                return Node(value) 
            elif value < parent.value: 
                parent.left = wrapper(parent.left) 
            else: 
                parent.right = wrapper(parent.right) 
            parent.height = 1 + max(self.getHeight(parent.left), self.getHeight(parent.right)) 
            balance = self.getBalance(parent) 
    
            if balance > 1 and value < parent.left.value: 
                return self.rightRotate(parent) 
    
            
            if balance < -1 and value > parent.right.value: 
                return self.leftRotate(parent) 
    
            
            if balance > 1 and value > parent.left.value: 
                parent.left = self.leftRotate(parent.left) 
                return self.rightRotate(parent) 
    
            
            if balance < -1 and value < parent.right.value: 
                parent.right = self.rightRotate(parent.right) 
                return self.leftRotate(parent) 
    
            return parent
        self.root = wrapper(self.root)
  
    def leftRotate(self, dis_node): 
        new_node = dis_node.right 
        dis_node.right = dis_node.right.left
        new_node.left = dis_node
        dis_node.height = 1 + max(self.getHeight(dis_node.left), self.getHeight(dis_node.right)) 
        new_node.height = 1 + max(self.getHeight(new_node.left), self.getHeight(new_node.right)) 
        return new_node 
  
    def rightRotate(self, dis_node): 
        new_node = dis_node.left 
        dis_node.left = dis_node.left.right
        new_node.right = dis_node
        dis_node.height = 1 + max(self.getHeight(dis_node.left), self.getHeight(dis_node.right)) 
        new_node.height = 1 + max(self.getHeight(new_node.left), self.getHeight(new_node.right)) 
  
        return new_node 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def out(self):
        def wrapper(parent):
            if not parent: 
                return
            wrapper(parent.left)
            print("{0} ".format(parent.value), end="")  
            wrapper(parent.right)
        wrapper(self.root)
            
  
  
myTree = AVL_Tree() 
parent = None
  
parent = myTree.add(10) 
parent = myTree.add(20) 
parent = myTree.add(30) 
parent = myTree.add(40) 
parent = myTree.add(50) 
parent = myTree.add(25)
myTree.out() 