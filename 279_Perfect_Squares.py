import math
from operator import mod
from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        lst=[]  # keeps the perfect squares
        initialStack=[]  # keeps track of the values
        uniqueSet=set()  # does not allow the repeatition of realized values and counts
        i=1
        while i*i<=n:
            initialStack.append((i*i,1))
            uniqueSet.add((i*i,1))
            lst.append(i*i)
            i+=1
        initialStack= deque(initialStack[::-1])
        while initialStack:
            val=initialStack.popleft()
            rlz=val[0]
            count=val[1]
            diff=n-rlz
            if not diff:
                return count
            else:
                k=0
                while k<len(lst) and lst[k]<=diff:  # The Meat
                    if lst[k]==diff:
                        return count+1 
                    elif (rlz+lst[k],count+1) not in uniqueSet:
                        initialStack.append((rlz+lst[k],count+1))
                        uniqueSet.add((rlz+lst[k],count+1))
                    k+=1

if __name__=="__main__":
    n=12
    print(Solution().numSquares(n=n))