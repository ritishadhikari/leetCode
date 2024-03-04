# VVI
from bisect import bisect_left
from typing import List
from math import inf

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        totalDiff=0
        diffList=[]
        mod=10**9 + 7
        best=inf
        n=len(nums1)
        
        for i in range(n):
            diff=abs(nums1[i]-nums2[i])
            totalDiff+=diff
            diffList.append(diff)
        nums1.sort()

        for i,num in enumerate(diffList):
            idx=bisect_left(a=nums1,x=nums2[i])
            if idx<n and nums1[idx]==nums2[i]:
                best=min(best, totalDiff-num)
            else:
                if idx>0: 
                    best=min(best, totalDiff-num+abs(nums2[i]-nums1[idx-1]))
                if idx<n: 
                    best=min(best,totalDiff-num+abs(nums2[i]-nums1[idx]))
        return best%mod

if __name__=="__main__":
    nums1 = [1,7,5]
    nums2 = [2,3,5]
    print(Solution().minAbsoluteSumDiff(nums1=nums1, nums2=nums2))