from typing import List
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        parent = list(range(n))
        rank = [0] * n
        
        for a, b in connections:
            while a != parent[a]:
                # a, parent[a] = parent[a], parent[parent[a]]
                t=a
                a=parent[a]
                n=parent[parent[t]]
                parent[t]=n
            while b != parent[b]:
                # b, parent[b] = parent[b], parent[parent[b]]
                t=b
                b=parent[b]
                n=parent[parent[t]]
                parent[t]=n
            
            if rank[a] == rank[b]:
                rank[a] += 1
            elif rank[a] < rank[b]:
                a, b, = b, a
            
            parent[b] = a
        
        count=0
        for i,v in enumerate(parent):
          if i==v:  count+=1
        return count-1


        return sum(parent[x] == x for x in range(n)) - 1

if __name__=="__main__":
  n = 8
  # connections = [[0,1],[0,2],[0,3],[1,2]]
  # connections=[[1,4],[1,5],[4,5],[3,4],[2,3]]
  connections=[[4,1],[3,1],[3,4],[5,4],[5,3]]
  connections=[[0,1],[0,3],[0,2],[2,3],[4,5],[4,6],[4,7],[0,4],[7,5]]
  print(Solution().makeConnected(n=n,connections=connections))