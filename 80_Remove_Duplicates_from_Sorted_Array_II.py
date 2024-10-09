from typing import List
from collections import Counter,OrderedDict
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq=OrderedDict(Counter(nums))
        extra=0
        index=0
        for val, count in freq.items():
            if count<=2:
                nums[index:index+count]=[val]*count
                index+=count
            else:
                nums[index:index+2]=[val]*2
                index+=2
                extra+=count-2
        return len(nums[:index])
        


if __name__=="__main__":
    nums =  [0,0,1,1,1,1,2,3,3]
    print(Solution().removeDuplicates(nums=nums))