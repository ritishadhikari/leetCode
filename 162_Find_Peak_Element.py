from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        
        while i<len(nums):
            if i!=0 and j!=len(nums)-1:
                if nums[i]>nums[i-1] and (i+1==len(nums) or nums[i]>nums[i+1]) : return i
                    
                if nums[j]>nums[j+1] and (j-1==-1 or nums[j]>nums[j-1]): return j
            i+=1
            j-=1
        return 0
if __name__=="__main__":
    nums = [1,2]
    print(Solution().findPeakElement(nums=nums))