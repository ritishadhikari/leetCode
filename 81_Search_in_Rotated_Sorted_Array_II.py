from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            if target>nums[m]:  # increase case 
                if target<=nums[r]:  # number lies between m and r
                    l=m+1
                elif (sum(nums[m:r+1])/len(nums[m:r+1]))<=nums[m]: # number lies on the opposite side
                    r=m-1
                else: l=m+1  
            elif target<nums[m]: # decrease case
                if target>=nums[l]: # number lies between l and m
                    r=m-1
                elif (sum(nums[l:m+1])/len(nums[l:m+1]))>=nums[l]: # number lies on the opposite side
                    l=m+1
                else: r=m-1   
            else: return True         
        return False

if __name__=="__main__":
    nums=[3,5,1]
    target=1
    print(Solution().search(nums=nums,target=target))