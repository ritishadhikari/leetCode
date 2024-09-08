# VVI
from typing import List
from math import inf
import heapq
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.address={i:set() for i in range(n)}
        for start,end,cost in edges:
           self.address[start].add((end,cost))

    def addEdge(self, edge: List[int]) -> None:
        start,end,cost=edge
        self.address[start].add((end,cost))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        queue=[(0,node1)]
        distance=[inf for i in range(len(self.address))]
        while queue:
            cost,node=heapq.heappop(queue)
            # owing to the heapq structure, the lowest cost node will always pop out
            if node==node2:
                return cost
            else:
                for neighbor,costing in self.address[node]:
                    newCost=costing+cost
                    # Only include interim node if the cost previous till this node
                    # is greater than the present cost of coming till this node
                    if distance[neighbor]>newCost:
                        distance[neighbor]=newCost
                        # push as per cost
                        heapq.heappush(queue,(newCost,neighbor))
        return -1        
        

if  __name__=="__main__":
    # n=13
    # initialEdges=[[7,2,131570],[9,4,622890],[9,1,812365],[1,3,399349],[10,2,407736],[6,7,880509],[1,4,289656],[8,0,802664],[6,4,826732],[10,3,567982],[5,6,434340],[4,7,833968],[12,1,578047],[8,5,739814],[10,9,648073],[1,6,679167],[3,6,933017],[0,10,399226],[1,11,915959],[0,12,393037],[11,5,811057],[6,2,100832],[5,1,731872],[3,8,741455],[2,9,835397],[7,0,516610],[11,8,680504],[3,11,455056],[1,0,252721]]
    # obj = Graph(n=n, edges=initialEdges)
    # print(obj.shortestPath(node1=9,node2=3))
    # print(obj.addEdge(edge=[11,1,873094]))
    # print(obj.shortestPath(node1=3,node2=10))
    # print(obj.addEdge(edge=[0,9,601498]))
    # print(obj.addEdge(edge=[12,0,824080]))
    # print(obj.addEdge(edge=[12,4,459292]))
    # print(obj.addEdge(edge=[6,9,7876]))
    # print(obj.addEdge(edge=[11,7,5479]))
    # print(obj.addEdge(edge=[11,12,802]))
    # print(obj.shortestPath(node1=2,node2=9))
    # print(obj.shortestPath(node1=2,node2=6))
    # print(obj.addEdge(edge=[0,11,441770]))
    # print(obj.shortestPath(node1=3,node2=7))

    obj=Graph(n=4,edges=[[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
    print(obj.shortestPath(node1=3,node2=2))
    print(obj.shortestPath(node1=0,node2=3))
    print(obj.addEdge(edge=[1,3,4]))
    print(obj.shortestPath(node1=0,node2=3))