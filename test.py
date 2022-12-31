from typing import List
import math

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1
        while left < right : 
            mid = left + (right - left) // 2
            count = 0
            for k in nums:
                if mid < k <= right:
                    count += 1
            if count > right - mid:
                left = mid + 1
            else:
                right = mid
        return right


if __name__=="__main__":
    nums=[1,3,4,5,2,2]
    print(Solution().findDuplicate(nums=nums))
