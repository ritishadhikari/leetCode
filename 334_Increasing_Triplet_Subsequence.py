# VVI
from typing import List
from math import inf
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first=inf
        second=inf
        for n in nums:
            if n<=first:
                first=n
            elif n<=second:
                second=n
            else:
                return True
        return False

            

if __name__=="__main__":
    nums=[5, 1, 5, 5,3,4] 
    nums=[2,3,1,4]
    print(Solution().increasingTriplet(nums=nums))