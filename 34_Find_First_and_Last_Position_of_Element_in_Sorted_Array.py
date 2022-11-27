# VVI
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        r=len(nums)-1
        l=0
        ans=-1
        res=[]
        # For the Start Index of the Target Number
        while l<=r:
            m=l+r>>1
            if nums[m]==target:
                ans=m
                r=m-1
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        if ans==-1: return [ans,ans]
        res.append(ans)
        l=ans
        r=len(nums)-1
        # For the End Index of the Target Number
        while l<=r:
            m=l+r>>1
            if nums[m]==target:
                ans=m
                l=m+1
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1
        res.append(ans)

        return res




if __name__=="__main__":
    nums = [5,7,8,8,8,8,9,10]
    target=8
    print(Solution().searchRange(nums=nums,target=target))