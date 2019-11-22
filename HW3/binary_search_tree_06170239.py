class TreeNode:
    def __init__(self,value):
        self.value = value
        self.leftchild = None
        self.rightchild = None
        
    def getval(self):
        return self.value
    
    def getright(self):
        return self.rightchild
    
    def getleft(self):
        return self.leftchild
        
class Solution(object):
    def __init__(self):
        self.root = None
    def insert(root,value):
        if root is None:
            root = TreeNode(value)
        else:
            current = root
            if current >= value:
                if current.leftchild == None:
                    current.leftchild = TreeNode(value)
                else:
                    insert(root.left,current.value)
            if current < value:
                if current.rightchild == None:
                    current.rightchild = TreeNode(value)
                else:
                    insert(root.right,current.value)
    
    def search(self,value):
        current = self.root.value
        if current == value:
            return current
        else:
            while current != value:
                if value <= current:
                    if current.leftchild is not None:
                        current = current.leftchild
                    else:
                        return "Not Exist at tree"
                if value > current:
                    if current.rightchild is not None:
                        current = current.rightchild
                    else:
                        return "Not Exist at tree"
            
            return current
        
    def delete(self,value):
        if self.root == None:
            return False
        if self.root.value == value:
            if self.root.leftchild is None and self.root.rightchild is None:
                self.root = None
                return
            elif self.root.leftchild and self.root.rightchild is None:
                self.root = self.root.leftchild
                return
            elif self.root.leftchild is None and self.rightchild:
                self.root = self.rightchild
                return
            else:
                temp = self.root.right
                temp_parent = None
                while temp.leftchild:
                    temp_parent=temp
                    temp = temp.leftchild
                self.root.value = temp.value
                if temp.value < temp_parent.value:
                      temp_parent.leftchild = None
                else:
                      temp_parent.rightchild = None
                return
                        
        parent = None
        node = self.root
        while node and node.value != value:
            parent = node
            if value < node.value:
                node = node.leftchild
            elif value > node.value:
                node = node.rightchild
        if node == None and node.value != value:
            return "Value not Found"
        
        if node.leftchild is None and node.rightchild is None:
            if value < parent.value:
                parent.leftchild = None
            else:
                parent.rightchild = None
                
            return
        
        if node.leftchild and node.rightchild is None:
            if value < parent.value:
                parent.leftchild = node.leftchild
            else:
                parent.rightchild = node.rightchild
                
            return
        
        if node.leftchild is None and node.rightchild:
            if value < parent.value:
                parent.leftchild = node.rightchild
            else:
                parent.leftchild = node.rightchild
            
            return
        
        if node.leftchild and node.rightchild:
            temp_parent = node
            temp = node.rightchild
            while temp.leftchild:
                temp_parent.leftchild = temp
                temp = temp.leftchild
            node.value = temp.value
            if temp.right:
                if temp.value < temp_parent.value:
                    temp_parent.leftchild = temp.rightchild
                else:
                    temp_parent.rightchild = temp.rightchild
                    
            else:
                if temp.value < temp_parent.value:
                    temp_parent.leftchild = None
                else:
                    temp_parent.rightchild = None
                
            return
        
    def modify(root,value,new_value):
        while self.root.value = value:
            root = delete(root,value)
            root = insert(root,new_val)
            return root
        
    
            
        
        
        
              
                        
                        
        
                
        
                    
    

   
                    
    
            
        
    
    
        

        
