from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trace={i:[] for i in range(1,n+1)}
        for cand,candT in trust:
            trace[cand].append(candT)
        
        # The Town Judge Trusts nobody
        cond=None
        for cand in trace:
            if not trace[cand]:
                cond=cand
                break
        
        if cond is None:
            return -1

        else:
            # Everybody (except for the town judge) trusts the town judge.
            for cand in trace:
                if cond not in trace[cand] and cond!=cand:
                    return -1
            return cond

if __name__=="__main__":
    n=3
    trust = [[1,3],[2,3],[3,1]]
    print(Solution().findJudge(n=n,trust=trust))
