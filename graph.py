from typing import Deque
import time
class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_direct={}
        for start, end in self.edges:
            if start in self.graph_direct:
                self.graph_direct[start].append(end)
            else:
                self.graph_direct[start]=[end]
        print(f"Graph Dict: {self.graph_direct}")
    
    def getPaths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_direct:
            return []

        paths = []
        for node in self.graph_direct[start]:
            if node not in path:
                newPaths = self.getPaths(start=node, end=end, path=path)
                for p in newPaths:
                    paths.append(p)
        return paths

    def getPaths1(self, start, end):
        elementStack=Deque()
        tempHoldElements=Deque()
        finalHoldElements=Deque()

        elementStack.append(start)
        tempHoldElements.append([start])

        while elementStack:
            node=elementStack.pop()
            listToAppend=tempHoldElements.pop()
            
            if node==end:
                finalHoldElements.appendleft(listToAppend)
            elif self.graph_direct.get(node):
                    for d in self.graph_direct.get(node):
                        elementStack.append(d)
                        tempHoldElements.append(listToAppend+[d])

        return list(finalHoldElements)

if __name__=="__main__":
    routes = [
        ("Mumbai", "Paris",),
        ("Mumbai", "Dubai",),
        ("Paris", "Dubai",),
        ("Paris", "New York",),
        ("Dubai", "New York",),
        ("Dubai", "Yumthang",),
        ("New York", "Toronto",),
        ("New York", "Yumthang")
    ]

    route_graph = Graph(edges=routes)

    start=time.time()
    print(route_graph.getPaths(start="Paris", end="Toronto"))
    print(time.time()-start)

    start=time.time()
    print(route_graph.getPaths1(start="Paris", end="Toronto"))
    print(time.time()-start)