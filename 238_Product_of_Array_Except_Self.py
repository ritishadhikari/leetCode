# VVI
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[1]*len(nums)
        suffix=1
        prefix=1

        for i in range(len(nums)):
            answer[i]*=prefix
            prefix*=nums[i]
            answer[-1-i]*=suffix
            suffix*=nums[-1-i]

        return answer


if __name__=="__main__":
    nums = [2,8,0,5,4]
    print(Solution().productExceptSelf(nums=nums))