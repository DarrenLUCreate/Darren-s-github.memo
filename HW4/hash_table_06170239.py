from Crypto.Hash import MD5

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None]*self.capacity
        
    def hashf(self,key):
        m = MD5.new()
        m.update(key.encode("utf-8"))
        x = int(m.hexdigest(),16)
        return x
    
    def add(self,key):
        index = self.hashf(key)%self.capacity
        node = self.data[index]
        while node:
            if node.val == key:
                return
            node = node.next
        newnode = ListNode(self.hashf(key))
        newnode.next = self.data[index]
        self.data[index] = newnode
        
    def remove(self,key):
        index = self.hashf(key)%self.capacity
        node = self.data[index]
        current = None
        while node is not None:
            if node.val == self.hashf(key):
                current = node
                del current
                node = node.next
                return
            else:
                node = node.next
            return       
        
    def contain(self,key):
        index = self.hashf(key)%self.capacity
        node = self.data[index]
        while node != None:
            if node.val == self.hashf(key):
                return True
            node = node.next
        return False
            
