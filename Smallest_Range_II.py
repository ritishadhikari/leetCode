# Skip this question
from typing import List
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        if k==0: 
            return max(nums)-min(nums)

        nums.sort()
        maxVal=nums[-1]-k
        minVal=nums[0]-k
        result=maxVal-minVal
        
        for i in range(len(nums)-1):
            maxVal=max(maxVal,nums[i]+k)
            minVal=min(nums[0]+k,nums[i+1]-k)
            result=min(result,maxVal-minVal)

        return result


if __name__=="__main__":
    nums=[1,4,11,3,7]
    k=3
    print(Solution().smallestRangeII(nums=nums, k=k))