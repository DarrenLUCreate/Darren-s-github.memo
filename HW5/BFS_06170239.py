from collections import defaultdict

class Graph:
    def __init__(self):
         self.graph = defaultdict(list) 
    def addEdge(self,u,v):
        self.graph[u].append(v) 
    def BFS(self, s):
        visited = [s]
        queue = [s]
        while queue:
            s = queue.pop(0)
            print(s, end= " ")
            for item in self.graph[s]:
                if item not in visited:
                    queue.append(item)
                    visited.append(item)
    def DFS(self,s):
        visited = []
        stack = [s]
        
        while stack:
            s = stack.pop()
            if s not in visited:
                print(s, end=" ")
                visited.append(s)
                
                for j in self.graph[s]:
                    stack.append(j)
