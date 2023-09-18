from typing import List
from heapq import heapify, heappop, heappush
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1=len(nums1)
        n2=len(nums2)
        sumIndexTracker=[(nums1[i]+nums2[0],i,0) for i in range(n1)]
        heapify(sumIndexTracker)
        answer=[]
        
        
        for _ in range(min(k, (n1*n2))):
            sum_,i,j=heappop(sumIndexTracker)
            answer.append([nums1[i],nums2[j]])
            if j<n2-1:
                heappush(sumIndexTracker,(nums1[i]+nums2[j+1],i,j+1))

        return answer
    
if __name__=="__main__":
    nums1=[6,7,11]
    nums2=[2,4,6]
    print(Solution().kSmallestPairs(nums1=nums1, nums2=nums2,k=4))