from typing import List
from collections import deque, defaultdict

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)<=2:
            return max(nums)
        else:
            hash={0:nums[0],1:nums[1]}
            val=0
            while val<=len(nums)-3:
                nextKey1=val+2
                nextKey2=val+3
                if val<len(nums)-3:
                    hash[nextKey1]=max(hash[val]+nums[nextKey1],hash.get(nextKey1,0))
                    hash[nextKey2]=max(hash[val]+nums[nextKey2],hash.get(nextKey2,0))
                else:
                    hash[nextKey1]=max(hash[val]+nums[nextKey1],hash.get(nextKey1,0))
                
                val+=1
        
            return max(hash.values())
    

if __name__=="__main__":
    number=[6,6,4,8,4,3,3,10]
    # number=[2,1,1,2]
    print(Solution().rob(nums=number))

  
