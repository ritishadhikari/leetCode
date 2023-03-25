from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        s=0
        for i in range(2,len(nums)+1,2):
            s+=min(nums[i-2:i])
        return s


if __name__=="__main__":
    nums = [6,2,6,5,1,2]
    print(Solution().arrayPairSum(nums=nums))