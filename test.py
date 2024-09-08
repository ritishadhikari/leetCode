from collections import defaultdict
from typing import List
import heapq 
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.hashmap = defaultdict(list)
        for src,des,w in edges:
            self.hashmap[src].append((des,w))
        

    def addEdge(self, edge: List[int]) -> None:
        src,des,w = edge
        self.hashmap[src].append((des,w))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        pq = [(0,node1)]
        distances = [float("inf")] * self.n
        distances[node1] = 0

        while pq:
            traveled,node = heapq.heappop(pq)

            if node == node2:
                return traveled
            
            for neighbor,w in self.hashmap[node]:
                newdis = traveled + w
                if newdis < distances[neighbor]:
                    distances[neighbor] = newdis
                    heapq.heappush(pq, (newdis,neighbor))
        return -1
    

if __name__=="__main__":
    obj=Graph(n=4,edges=[[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
    print(obj.shortestPath(node1=3,node2=2))
    print(obj.shortestPath(node1=0,node2=3))
    print(obj.addEdge(edge=[1,3,4]))
    print(obj.shortestPath(node1=0,node2=3))
    
