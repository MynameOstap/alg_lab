class TreeNode: 
    def __init__(self, val): 
        self.value = val 
        self.left = None
        self.right = None
        self.height = 1
  
 
class AVL_Tree: 
  
    
    def add(self, root, value): 
      
         
        if not root: 
            return TreeNode(value) 
        elif value < root.value: 
            root.left = self.add(root.left, value) 
        else: 
            root.right = self.add(root.right, value) 
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right)) 
        balance = self.getBalance(root) 
  
        if balance > 1 and value < root.left.value: 
            return self.rightRotate(root) 
  
         
        if balance < -1 and value > root.right.value: 
            return self.leftRotate(root) 
  
        
        if balance > 1 and value > root.left.value: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        
        if balance < -1 and value < root.right.value: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
  
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
  
    def out(self, root): 
        if not root: 
            return
        self.out(root.left)
        print("{0} ".format(root.value), end="")  
        self.out(root.right)
         
  
  
myTree = AVL_Tree() 
root = None
  
root = myTree.add(root, 10) 
root = myTree.add(root, 20) 
root = myTree.add(root, 30) 
root = myTree.add(root, 40) 
root = myTree.add(root, 50) 
root = myTree.add(root, 25)
myTree.out(root) 