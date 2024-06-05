from typing import List
from heapq import (heapify,heappop,
                   heappushpop,heappush,heapreplace)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapify(self.nums)
        while len(self.nums)>k:
            heappop(self.nums)
                
    def add(self, val: int) -> int:
        if len(self.nums)<self.k:
            heappush(self.nums,val)
        elif val>self.nums[0]:
            heapreplace(self.nums,val)
        return self.nums[0]
        
if __name__=="__main__":
    obj=KthLargest(k=3,nums=[4, 5, 8, 2])
    print(obj.add(val=3))
    print(obj.add(val=5))
    print(obj.add(val=10))
    print(obj.add(val=9))
    print(obj.add(val=4))
