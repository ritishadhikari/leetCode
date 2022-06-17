from typing import List
from collections import Counter

class Solution():
    def singleNumber(self,nums:List[int]) -> int:
        mapdict={}
        size=len(nums)
        for i in range(size):
            if nums[i] not in mapdict:
                mapdict[nums[i]]=i
            else:
                # Make MapDict Position Zero
                nums[mapdict[nums[i]]]=0
                # Make Current Position Zero
                nums[i]=0

        return sum(nums)


if __name__=="__main__":
    number=[1,0,1]
    print(Solution().singleNumber(nums=number))