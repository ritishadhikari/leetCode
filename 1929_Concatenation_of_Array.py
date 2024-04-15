from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums


if __name__=="__main__":
    nums=[1,3,2,1]
    print(Solution().getConcatenation(nums=nums))