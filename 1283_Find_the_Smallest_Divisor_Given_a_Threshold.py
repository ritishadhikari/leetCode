from typing import List
from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=1
        r=max(nums)
        def valid(guess):
            count=0
            for n in nums:
                count+=ceil(n/guess)
                if count>threshold: return False
            return True
        best=r
        while l<=r:
            m=(l+r)//2
            if valid(guess=m):
                r=m-1
                best=min(best,m)
            else:
                l=m+1
        return best

if __name__=="__main__":
    nums = [21212,10101,12121]
    threshold=1000000
    print(Solution().smallestDivisor(nums=nums,threshold=threshold))