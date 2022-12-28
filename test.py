from typing import List
import math

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        
        def count(d):
            ans, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            return ans
        
        l, r = 0, position[-1] - position[0]
        while l < r:
            # mid = r - (r - l) // 2
            mid=(r+l)//2+1
            # mid=l+(r-l)//2
            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l


if __name__=="__main__":
    position=[5,4,3,2,1,1000000000]
    m=2
    print(Solution().maxDistance(position=position,m=m))
