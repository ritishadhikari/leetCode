# VVI
from typing import List
import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l=1
        # r=10**7
        r=max(max(dist),int(dist[-1]/0.01))
        best=None
        def valid(guess):
            tot=0
            for d in dist:
                hr=d/guess
                if tot+hr>hour: return False
                tot+=math.ceil(hr)
            return True


        while l<=r:
            m=(l+r)//2
            if valid(m):
                r=m-1
                best=m
            else:
                l=m+1
        return best if best is not None else -1

if __name__=="__main__":
    dist = [1,1,100000]
    hour=2.01
    print(Solution().minSpeedOnTime(dist=dist, hour=hour))