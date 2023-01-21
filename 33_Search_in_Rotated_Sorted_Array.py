from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            if target>nums[m]:  # increase case 
                if target<=nums[r]:  # number lies between m and r
                    l=m+1
                else:
                    if nums[r]>=nums[m]: # number lies on the opposite side
                        r=m-1
                    else: l=m+1  
            elif target<nums[m]: # decrease case
                if target>=nums[l]: # number lies between l and m
                    r=m-1
                else:
                    if nums[l]<=nums[m]: # number lies on the opposite side
                        l=m+1
                    else: r=m-1   
            else: return m         
        return -1
        

if __name__=="__main__":
    nums = [1,0,1,1,1]
    target=3
    print(Solution().search(nums=nums,target=target))