from typing import List
class Solution:
     def eventualSafeNodes(self, g: List[List[int]]) -> List[int]:
        n=len(g)
        ing=[[] for _ in range(n)]
        outd=[0]*n

        q=[]
        for o,ins in enumerate(g):
            outd[o]=len(ins)
            if outd[o]==0:  q.append(o) 
            for i in ins:   ing[i].append(o)
                   
        res=[]
        while (q):
            node= q.pop()
            res.append(node)

            for ins in ing[node]:
                outd[ins]-=1 
                if outd[ins]==0: q.append(ins)


        return sorted(res)
       
if __name__=="__main__":
  g=[[1,2,3,4],[1,2],[3,4],[0,4],[]]
  print(Solution().eventualSafeNodes(g=g))