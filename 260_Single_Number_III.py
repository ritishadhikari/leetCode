from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ones,twos=set(),set()
        for n in nums:
            if n not in ones:
                ones.add(n)
            else:
                twos.add(n)
        return list(ones.difference(twos))

if __name__=="__main__":
    nums=[0,1]
    print(Solution().singleNumber(nums=nums))