from typing import List
from math import inf
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minL=inf
        l=0
        r=0
        s=nums[l]
        lastOps=None
        while l<=r and r<len(nums):
            if lastOps=="l": s-=nums[l-1]
            elif lastOps=="r": s+=nums[r]
            
            if s<target:
                r+=1
                lastOps="r"
            else:
                minL=min(minL,r-l+1)
                l+=1
                lastOps="l"
        return minL if minL is not inf else 0
if __name__=="__main__":
    target = 7
    nums = [2,3,1,2,4,3]
    print(Solution().minSubArrayLen(target=target,nums=nums))