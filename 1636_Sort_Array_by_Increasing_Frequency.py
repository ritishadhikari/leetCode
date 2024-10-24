from typing import List
from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq=sorted(Counter(nums).items(),key=lambda k:[k[1],-k[0]])
        ans=[]
        for num,freq in freq:
            ans+=[num]*freq
        return ans
if __name__=="__main__":
    nums = [2,3,1,3,2]
    print(Solution().frequencySort(nums=nums))