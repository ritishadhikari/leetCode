from typing import List
from collections import deque
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack=deque()
        finalStack=deque()
        
        num=n-k
        numTotal=1
        for i in range(n,num,-1):
            numTotal*=i
        
        denomTotal=1
        for i in range(k,0,-1):
            denomTotal*=i
            
        totalLength=numTotal//denomTotal
        
        for i in range(1,n+1):
            stack.append([i])
            while stack:
                pointer=stack.popleft()
                if len(pointer)==k:
                    finalStack.append(pointer)
                    if len(finalStack)==totalLength:
                        return finalStack
                elif len(pointer)<k and pointer[-1]<n:
                    for j in range(pointer[-1]+1,n+1):
                        stack.append(pointer+[j])
                        
        return finalStack


if __name__=="__main__":
    n=4
    k=3
    print(Solution().combine(n=n,k=k))