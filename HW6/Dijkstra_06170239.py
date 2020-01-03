from collections import defaultdict

class Graph():
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
        
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i])
    
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
        
    def Dijkstra(self, s):
        Passed = dict()
        row = [i for i in enumerate(self.graph[s])]
        
        
        
        
        
    def Kruskal(self):
        n = [] ; a = []
        result = dict(zip(n,a))
        i = 0
        e = 0
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
        for node in range(self.V): 
            n.append(node) 
            a.append(0)
        while e < self.V -1 :
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(n, u) 
            y = self.find(n ,v) 
            
            if x != y: 
                e = e + 1     
                name = str(u)+'-'+str(v)
                result[name] = w
                self.union(n, a, x, y)
            
        return result
                
        
