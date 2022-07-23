from typing import List
from math import inf
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length=len(nums)
        valueList=[0 for _ in range(length)]
        minimumVal=nums[0]

        for i in range(length):
            valueList[i]+=1
            if i:
                negIRepresent=-(length-i)
                if not nums[i]<minimumVal:
                    for j in range(negIRepresent-1,-length-1,-1):
                        if nums[i]>nums[j]:
                            valueList[i]=max(valueList[i],valueList[j]+1)
                else:
                    minimumVal=nums[i]
        
        return max(valueList)



if __name__=="__main__":
    nums = [10,9,2,5,3,7,101,18,4,102,103]
    nums=[0,1,0,3,2,3]
    print(Solution().lengthOfLIS(nums=nums))