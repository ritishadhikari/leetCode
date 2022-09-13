from typing import List
from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        traceDict=defaultdict(lambda : [])
        for i,val in enumerate(nums):
            if val in traceDict.keys():
                for j in traceDict[val]:
                    if abs(j-i)<=k:
                        return True
            traceDict[val].append(i)
           
        return False

if __name__=="__main__":
    nums=[1,2,3,1,2,3]
    k=2
    print(Solution().containsNearbyDuplicate(nums=nums, k=k))
