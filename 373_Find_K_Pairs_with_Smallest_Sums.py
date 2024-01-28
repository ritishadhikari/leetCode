import pandas as pd
from heapq import heappop,heappush,heapify
from typing import List
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1=len(nums1)
        n2=len(nums2)
        sumIndexTracker=[(nums1[0]+nums2[j],0,j) for j in range(n2)]
        heapify(sumIndexTracker)
        answer=[]
        for _ in range(min(k, (n1*n2))):
            sum_,i,j=heappop(sumIndexTracker)
            answer.append([nums1[i],nums2[j]])
            if i<n1-1:
                heappush(sumIndexTracker,(nums1[i+1]+nums2[j],i+1,j))

        return answer


if __name__=="__main__":
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k=3
    print(Solution().kSmallestPairs(nums1=nums1,nums2=nums2,k=k))