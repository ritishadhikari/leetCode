from typing import List
from collections import Counter, deque

class Solution:
    def moveZeroes(self, nums:List[int]) -> None:

        noOfzeros=Counter(nums)[0]  # Dictionary Consumes Space
        lst=[]  # List Consumes Space

        for val in nums:
            if val:
                lst.append(val)
        
        for i in range(noOfzeros):
            lst.append(0)        
        
        nums[:]=lst

        # Alternate Solution
        
        i=0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
        


if __name__=="__main__":
    nums=[0,1,0,3,12]
    print(id(nums))

    Solution().moveZeroes(nums=nums)
    print(nums)
    print(id(nums))
