from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        for ch in operations:
            if len(res) and ch=="+":
                res.append(res[-1]) if len(res)==1 else res.append(res[-1]+res[-2])
            elif len(res) and ch=="D":  res.append(2*res[-1])
            elif len(res) and ch=="C":  res.pop()
            else:   res.append(int(ch))
        return sum(res)
            


if __name__=="__main__":
    ops=["1","C"]
    print(Solution().calPoints(operations=ops))