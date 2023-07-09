import heapq 
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return sorted(nums)[-k]
        length=len(nums)
        heapq.heapify(nums)

        for i in range(length-k+1):
            if i==length-k:
                return heapq.heappop(nums)
            heapq.heappop(nums)

if __name__=="__main__":
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    print(Solution().findKthLargest(nums=nums, k=k))