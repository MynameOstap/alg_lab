class Node:
    def __init__(self,value):
        self.right:Node = None
        self.left:Node = None
        self.value = value
        self.height:int = 1

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def add(self,value):
        node = Node(value)
        parent = self.__find(value, self.root)
        
        if parent is None:
            self.root = node
            return
        if parent.value == value:
            raise Exception
        if parent.value > value:
            parent.left = node
        else:
            parent.right = node
        parent.height = max(parent.height - 1, 1) + 1
            
        
    def __find(self,value,parent) -> Node:
        if parent is None:
            return None
        child = parent.left if parent.value > value else parent.right
        if child is None:
            return parent
        return self.__find(value, child)
        
    def find(self,value):
        node = self.__find(value,self.root)
        if node is None:
            return None
        if node.value == value:
            return value
        return None
    def detour(self):
        out = ' '
        def inner(parent):
            nonlocal out
            if parent is None:
                return
            inner(parent.left)
            out += str(parent.value) + ' ' 
            inner(parent.right) 
        inner(self.root)
        return out
        
        
import random
t = BinaryTree()

for _ in range(50):
    try:
        t.add(random.randint(0, 255))
    except:
        ...
print(t.detour())        
print(t.find(144))
        
        
        
    

        
        
        
        