from typing import List
from collections import defaultdict
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        traceList=[]
        for event in graph[0]:
            traceList.append([0]+[event])
        finalList=[]
        while traceList:
            seq=traceList.pop()
            lastIndex=seq[-1]
            if lastIndex==len(graph)-1:
                finalList.append(seq)
            else:
                for event in graph[lastIndex]:
                    traceList.append(seq+[event])
        return finalList
        

if __name__=="__main__":
    graph = [[1,2],[3],[3],[]]
    print(Solution().allPathsSourceTarget(graph=graph))