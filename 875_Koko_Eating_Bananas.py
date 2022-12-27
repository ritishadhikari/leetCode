from typing import List
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid(guess):
            count=0
            for p in piles:
                count+=ceil(p/guess)
                if count>h: return False
            return True

        l=1
        r=max(piles)
        most=r

        while l<=r:
            m=(l+r)//2
            if valid(guess=m):
                r=m-1
                most=min(m,most)
            else:
                l=m+1
        return most

if __name__=="__main__":
    piles = [312884470]
    h=5
    print(Solution().minEatingSpeed(piles=piles, h=h))