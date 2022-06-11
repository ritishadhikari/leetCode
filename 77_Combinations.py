from typing import List
from collections import deque
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack=deque([[i] for i in range(1,n+1)])
        while stack:
            if len(stack[0])==k:
                return stack
            else:
                pointer=stack.popleft()
                j=pointer[-1]+1
                while j<=n:
                    stack.append(pointer+[j])
                    j+=1


if __name__=="__main__":
    n=4
    k=2
    print(Solution().combine(n=n,k=k))