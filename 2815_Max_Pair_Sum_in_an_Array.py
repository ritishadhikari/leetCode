from typing import List
from collections import Counter
from math import inf

class Solution:

    def splitService(self,nums):
        return Counter(str(nums))


    def maxSum(self, nums: List[int]) -> int:
        maxNums=-1
        seen=set()
        numsSize=len(nums)
        for ind,numP in enumerate(nums[:numsSize-1]):
            seen.add(numP)
            for numS in nums[ind+1:numsSize]:
                if numS not in seen:
                    if self.splitService(nums=numP)\
                        ==self.splitService(nums=numS):
                        seen.add(numS)
                        maxNums=max(maxNums,numS+numP)
        return maxNums
            


if __name__=="__main__":
    nums=[1,2,3,4]
    print(Solution().maxSum(nums=nums))