from typing import List
from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        else:
            traceList=[]
            for s in digits:
                
                if s in ["1","2","3","4","5","6"]:
                    traceList.append([chr(97+((int(s)-2)*3+k)) for k in range(3)])
                elif s in ["7"]: traceList.append(["p","q","r","s"])
                elif s in ["8"]: traceList.append(["t","u","v"])
                elif s in ["9"]: traceList.append(["w","x","y","z"])

        return [''.join(m) for m in list(product(*traceList))]

if __name__=="__main__":
    digits="234"
    print(Solution().letterCombinations(digits=digits))