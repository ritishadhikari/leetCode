from collections import deque
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rangeVal=nums.copy()
        nums=deque([[i] for i in nums])
        while nums:
            if len(nums[0])==len(rangeVal):
                return nums
            else:
                val=nums.popleft()
                for i in rangeVal:
                    if i not in val:
                        nums.append(val+[i])

if __name__=="__main__":
    nums=[0,1,2]
    print(Solution().permute(nums=nums))