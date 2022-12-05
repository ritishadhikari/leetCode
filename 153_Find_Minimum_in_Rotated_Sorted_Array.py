from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        m=(l+r)//2
        while l<=r:
            if nums[l]==nums[m] and nums[m]==nums[r]:
                return nums[m]
            elif nums[m]>nums[l] and nums[m]<nums[r]:  # normal ascending matrix
                r=m-1
            elif nums[m]<nums[l] and nums[m]<nums[r]:  # min in the left half
                r=m
            elif nums[m]>nums[l] and nums[m]>nums[r]:  # min in the right half
                l=m
            elif nums[m]==nums[l] and nums[m]>nums[r]:  # min is to the right of left
                l=r
            elif nums[m]==nums[l] and nums[m]<nums[r]:  # min is to the left of right
                r=l 
            elif nums[m]>nums[l] and nums[m]==nums[r]: # min is to the left of right
                r=l
            elif nums[m]<nums[l] and nums[m]==nums[r]: # min is to the right of left
                l=r
            m=(l+r)//2

if __name__=="__main__":
    nums=[0,1]
    print(Solution().findMin(nums=nums))