# VVI

from typing import List
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:    return -1
        else:
            parent=list(range(n))
            rank=[0]*n
            for a,b in connections:
                while a!=parent[a]:  # tracking the source
                    t=a
                    a=parent[a]
                    n=parent[parent[t]]
                    parent[t]=n
                while b!=parent[b]:  # tracking the source
                    t=b
                    b=parent[b]
                    n=parent[t]
                    b=parent[t] 
                if rank[a]==rank[b]:        
                    rank[a]+=1
                elif rank[a]<rank[b]:
                    a,b=b,a
                
                parent[b]=a  # The destination will always take the identity of the source
        
            count=0
            for i,v in enumerate(parent):
                if i==v:    count+=1

            return count-1

if __name__=="__main__":
    n=8
    connections=[[0,1],[0,3],[0,2],[2,3],[4,5],[4,6],[4,7],[0,4],[7,5]]
    print(Solution().makeConnected(n=8, connections=connections))