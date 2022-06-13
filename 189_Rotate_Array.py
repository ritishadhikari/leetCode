from typing import List
from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # d = deque(nums)

        # for _ in range(k):
        #     d.appendleft(d.pop())
        # nums[:]=list(d)

        k = k % len(nums)
        print(k)
        nums[:] = nums[-k:] + nums[:-k] 


if __name__=="__main__":
    nums=[1,2]
    Solution().rotate(nums=nums,k=3)
    print(nums)
