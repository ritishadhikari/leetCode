from typing import List
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)>1:
            nums=[(nums[i]+nums[i+1])%10 for i,num in enumerate(nums[:-1])]
        return nums[0]%10
    
if __name__=="__main__":
    nums = [5]
    print(Solution().triangularSum(nums=nums))
