from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]>nums[l] and nums[m]<nums[r]:  # normal ascending matrix [1,2], [1,2,3,4,5,6,7]
                r=m-1
            elif nums[m]<nums[l] and nums[m]<nums[r]:  # min in the left half [12,11,7,8,9], [6,7,1,2,3,4,5]
                r=m
            elif nums[m]>=nums[l] and nums[m]>=nums[r]:  # min in the right half [4,5,6,7,0,1,2], [3,4,5,6,7,1,2]
                l=m+1
        return nums[m]

if __name__=="__main__":
    nums=[4,5,6,7,0,1,2]
    print(Solution().findMin(nums=nums))