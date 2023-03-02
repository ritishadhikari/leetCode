from typing import List
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        seen=set()
        nums.sort()
        while nums:
            minNumber=nums.pop(0)
            if len(nums)==0:
                maxNumber=minNumber
            else:
                maxNumber=nums.pop()
            average=(minNumber+maxNumber)/2
            if average not in seen:
                seen.add(average)
        return len(seen)

if __name__=="__main__":
    nums = [4,1,0,3,5]
    print(Solution().distinctAverages(nums=nums))