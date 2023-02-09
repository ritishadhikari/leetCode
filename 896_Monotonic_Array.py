from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        incCase=True
        # Test for Increase Case
        for i,num in enumerate(nums):   
            if i>0:
                if num<last: 
                    incCase=False
                    break
            last=num
        
        if incCase:
            return True
        else:
            # Test for Decrease Case
            decCase=True
            for j,num in enumerate(nums):
                if j>0:
                    if num>last:
                        decCase=False
                        break
                last=num
            return True if decCase else False
        
        



if __name__=="__main__":
    nums = [1,3,2]
    print(Solution().isMonotonic(nums=nums))