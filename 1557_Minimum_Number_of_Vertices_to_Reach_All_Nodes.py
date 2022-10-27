import trace
from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        traceDict={i:0 for i in range(n)}

        for s,d in edges:
            traceDict[d]+=1
        
        out=[l for l in traceDict if traceDict[l]==0]
        
        return out
if __name__=="__main__":
    n =5
    edges = [[1,3],[2,0],[2,3],[1,0],[4,1],[0,3]]   
    print(Solution().findSmallestSetOfVertices(n=n,edges=edges))