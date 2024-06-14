from typing import List
from math import inf
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        maxVal=-inf
        count=0
        for n in nums:
            if n > maxVal:
                maxVal=max(maxVal,n)
            else:
                maxVal+=1
                count+=(maxVal-n)
        return count
if __name__=="__main__":
    nums = [3,2,1,2,1,7]
    print(Solution().minIncrementForUnique(nums=nums))