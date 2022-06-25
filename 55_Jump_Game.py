from typing import List
from collections import defaultdict

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True

if __name__=="__main__":
    nums=[3,2,1,0,4]
    print(Solution().canJump(nums=nums))