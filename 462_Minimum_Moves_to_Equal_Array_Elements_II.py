from typing import List
from statistics import median

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        length=len(nums)
        if length%2==1:
            median=nums[length//2]
        else:
            median=(nums[(length//2)]+nums[(length//2)-1])//2
        
        total=0
        for n in nums:
            total+=abs(n-median)
        return total

if __name__=="__main__":
    nums = [1,10,2,9]
    print(Solution().minMoves2(nums=nums))