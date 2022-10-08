from typing import List
from collections import deque
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        stack=deque([[cand] for cand in candidates])
        while stack:
            val=stack.popleft()
            if sum(val)==target:
                res.append(val)
            else:
                for cand in candidates:
                    if sum(val)+cand==target:
                        if sorted(val+[cand]) not in res:
                            res.append(sorted(val+[cand]))
                    elif sum(val)+cand<target:
                        if sorted(val+[cand]) not in stack:
                            stack.append(sorted(val+[cand]))
                    else:
                         break
        return res


if __name__=="__main__":
    candidates = [2,3,5]
    target = 8
    print(Solution().combinationSum(candidates=candidates, target=target))