from operator import mod


class Solution:
    def integerBreak(self, n: int) -> int:
        maxVal=0
        repeat=False
        for numOfParts in range(2,n+1):
            idealVal=n//numOfParts
            if idealVal==1:
                if not repeat:
                    total=idealVal*(n-idealVal)
                    repeat=True
                else:
                    break
            else:
                addedVal=mod(n,numOfParts)
                total=(idealVal+1)**addedVal*(idealVal**(numOfParts-addedVal))
            maxVal=max(total,maxVal)
        return maxVal


if __name__=="__main__":
    n=8
    print(Solution().integerBreak(n=n))