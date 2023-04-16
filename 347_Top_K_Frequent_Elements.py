from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k:int) -> List[int]:
        c=Counter(nums)
        return [l[0] for l in c.most_common(n=k)]

if __name__=="__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    print(Solution().topKFrequent(nums=nums, k=k))