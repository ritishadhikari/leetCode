# Can skip
from typing import List
from math import inf,ceil
class Solution:
    def minimumSize(size, nums:List[int], maxOperations:int) -> int:
        
        def valid(guess):
            count=0
            for num in nums:
                if num>guess:
                    count+=ceil(num/guess)-1
                    if count>maxOperations: return False
            return True

        l=1
        r=max(nums)
        best=r
        while l<=r:
            m=(l+r)//2
            if valid(guess=m):
                r=m-1
                best=min(best,m)
            else:
                l=m+1
        return best
    
    
    

if __name__=="__main__":
    nums=[2,4,8,2]
    maxOperations=4
    print(Solution().minimumSize(nums=nums, maxOperations=maxOperations))