from typing import List
from bisect import bisect_left
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        
        def getRemainingIndices(startingIndex):
            '''
                Using Linear Search to find the same next values
            '''
            lst=[]
            while startingIndex<len(nums):
                if nums[startingIndex]==target: 
                    lst.append(startingIndex)
                    startingIndex+=1
                else: break
            return lst
        
        def getRemainingIndices(startingIndex):
            '''
                Using Binary Search to find the same next Values
            '''
            lst=[]
            if startingIndex<len(nums) and nums[startingIndex]==target:
                l=startingIndex
                r=len(nums)-1
                while l<=r:
                    m=(l+r)//2
                    if nums[m]==target: 
                        lst+=list(range(l,m+1))
                        l=m+1
                    else:r=m-1
            return lst
        
        nums.sort()
        
        index=bisect_left(a=nums,x=target)
        return getRemainingIndices(startingIndex=index)
        

if __name__=="__main__":
    nums=[2,1,2,5,2,3,2]
    target=2
    print(Solution().targetIndices(nums=nums,target=target))