from typing import List
from collections import deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        q=set()
        for i in range(len(graph)):   
            q.add((i,tuple(set([i]))))
        
        steps=0
        while q:
            num=len(q)
            newSet=set()
            for j in range(num):
                node,visit=q.pop()
                if len(visit)==len(graph): return steps
                else:
                    for n in graph[node]:
                        v=set(visit).copy()
                        v.add(n)
                        if len(v)==len(graph): return steps+1
                        else:
                            if (n,tuple(v)) not in newSet: newSet.add((n,tuple(v)))
            q.update(newSet)
            if q: steps+=1
        

if __name__=="__main__":
    graph = [
            [1,2,3,4,5,6,7,8,9],
            [0,2,3,4,5,6,7,8,9],
            [0,1,3,4,5,6,7,8,9],
            [0,1,2,4,5,6,7,8,9],
            [0,1,2,3,5,6,7,8,9],
            [0,1,2,3,4,6,7,8,9],
            [0,1,2,3,4,5,7,8,9],
            [0,1,2,3,4,5,6,8,9],
            [0,1,2,3,4,5,6,7,9,10],
            [0,1,2,3,4,5,6,7,8,11],
            [8],
            [9]
            ]
    print(Solution().shortestPathLength(graph=graph))