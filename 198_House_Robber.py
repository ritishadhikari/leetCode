from typing import List
from collections import deque, defaultdict

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)<=2:
            return max(nums)
        else:
            hash={0:nums[0],1:nums[1]}
      
            nextKey1=2
            nextKey2=3
            val=0
            while nextKey2<=len(nums):
                if nextKey2<len(nums):
                    hash[nextKey1]=max(hash[val]+nums[nextKey1],hash.get(nextKey1,0))
                    hash[nextKey2]=max(hash[val]+nums[nextKey2],hash.get(nextKey2,0))
                else:
                    hash[nextKey1]=max(hash[val]+nums[nextKey1],hash.get(nextKey1,0))
                
                nextKey1+=1
                nextKey2+=1
                val+=1
        
            return max(hash.values())
    

if __name__=="__main__":
    number=[6,6,4,8,4,3,3,10]
    # number=[2,1,1,2]
    print(Solution().rob(nums=number))

  
