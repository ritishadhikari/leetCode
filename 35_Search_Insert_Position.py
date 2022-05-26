from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target: 
                if mid<r and nums[mid+1]>target:
                    return mid+1
                else:
                    l=mid+1
            elif nums[mid]>target:
                if mid>l and nums[mid-1]<target:
                    return mid
                else:
                    r=mid-1
        
        if r<0:
            return 0
        else:
            return len(nums)
        

if __name__=="__main__":
    nums=[1,3,5,7,9,11]
    print(Solution().searchInsert(nums=nums,target=6))