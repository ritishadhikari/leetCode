from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        if n==0:
            return [-1,-1]
        l=0
        h=n-1
        a=[]
        ans=-1
        #For checking the leftmost index
        while l<=h:
            m=(l+h)>>1
            if nums[m]==target:
                ans=m
                h=m-1
            elif nums[m]>target:
                h=m-1
            else:
                l=m+1
        #For checking the rightmost index
        a.append(ans)
        l=ans
        h=n-1
        while l<=h:
            m=(l+h)>>1
            if nums[m]==target:
                ans=m
                l=m+1
            elif nums[m]<target:
                l=m+1
            else:
                h=m-1
        a.append(ans)
        return a

if __name__=="__main__":
    nums = [5,7,8,8,8,8,9,10]
    target=6
    print(Solution().searchRange(nums=nums,target=target))