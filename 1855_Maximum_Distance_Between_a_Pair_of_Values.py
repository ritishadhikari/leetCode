from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i=0
        j=0
        maxDiff=0
        while i<len(nums1) and j<len(nums2):
            if i<=j:
                if nums1[i]<=nums2[j]:
                    maxDiff=max(maxDiff,(j-i))
                    j+=1
                else:
                    i+=1
            else:
                j+=1
        return maxDiff
if __name__=="__main__":
    nums1 = [9914,9434,8808,8041,7548,6727,5637,4635,2937,607,384,335]
    nums2 = [9980,9826,9620,9600,9455,9448,9374,9367,9278,9251,9083,8987,8952,8932,8762,8705,8595,8460]
    # nums1=[13,12,11]
    # nums2=[15,13,10]
    print(Solution().maxDistance(nums1=nums1, nums2=nums2))
