from typing import List
from collections import Counter
class Solution:
    def  majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        mc=count.most_common(n=1)[0]
        
        if mc[1]>len(nums)//2:
            return mc[0]
        else:
            return 0
          
        

if __name__=="__main__":
    nums = [2,2,1,1,1,2,2,3,3,9,3]
    print(Solution().majorityElement(nums=nums))