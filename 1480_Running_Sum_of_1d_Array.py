from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i:
                nums[i]=nums[i]+nums[i-1]
        return nums

if __name__=="__main__":
    nums=[3,1,2,10,1]
    print(Solution().runningSum(nums=nums))