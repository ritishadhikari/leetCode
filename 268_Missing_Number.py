from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        totalL=max(len(nums), max(nums))
        expectedSum=(totalL*(totalL+1))//2
        return expectedSum-sum(nums)

if __name__=="__main__":
    nums=[3,0,1]
    print(Solution().missingNumber(nums=nums))