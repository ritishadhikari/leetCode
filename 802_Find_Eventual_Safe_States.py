# VVI
from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        numberOfNodes=[0]*len(graph)
        destToSourceMap=[set() for _ in range(len(graph))]
        terminalNodes=set()
        for index, destinations in enumerate(graph):
            numberOfNodes[index]=len(destinations)
            if len(destinations)==0: terminalNodes.add(index)
            for destination in destinations: 
                destToSourceMap[destination].add(index)
        
        res=[]
        while terminalNodes:
            node=terminalNodes.pop()
            res.append(node)
            for source in destToSourceMap[node]:
                numberOfNodes[source]-=1
                if numberOfNodes[source]==0:
                    terminalNodes.add(source)
        return sorted(res)



if __name__=="__main__":
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    print(Solution().eventualSafeNodes(graph=graph))
