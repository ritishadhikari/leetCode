from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        td={}
        for a,b in dislikes:
            if a not in td: td[a]=[]
            td[a].append(b)
            if b not in td: td[b]=[]
            td[b].append(a)
        
        sets={'a':set(),'b':set()}
        for i in range(1,n+1):
            q=[i]
            sets['a'].add(i)
            while q:
                cand=q.pop()
                if cand in sets['a'] and cand in td:
                    for enem in td[cand]:
                        if enem in sets['a']:   return False
                        else:   
                            sets['b'].add(enem)
                            q.append(enem)
                    td.pop(cand)
                elif cand in sets['b'] and cand in td:
                    for enem in td[cand]:
                        if enem in sets['b']:   return False
                        else: 
                            sets['a'].add(enem)
                            q.append(enem)
                    td.pop(cand)
        return True
            


if __name__=="__main__":
    n = 5
    dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
    print(Solution().possibleBipartition(n=n,dislikes=dislikes))