from typing import List
from bisect import bisect_left
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        
        def getRemainingIndices(startingIndex):
            lst=[]
            while startingIndex<len(nums):
                if nums[startingIndex]==target: 
                    lst.append(startingIndex)
                    startingIndex+=1
                else: break
            return lst
        
        nums.sort()
        
        index=bisect_left(a=nums,x=target)
        return getRemainingIndices(startingIndex=index)
        




if __name__=="__main__":
    nums=[1,2,5,2,3]
    target=5
    print(Solution().targetIndices(nums=nums,target=target))