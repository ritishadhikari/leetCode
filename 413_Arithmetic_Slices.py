from typing import List
from collections import deque

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)<3:
            return  0
        else:
            size=len(nums)
            totalLength=0
            count=0
            while count<size-2:
                stack=deque([[nums[count], nums[count+1]]])
                nextCount=count+2
                diffVal=nums[count+1]-nums[count]
                while stack and nextCount<size:
                    elements=stack.popleft()
                    if nums[nextCount]-elements[-1]==diffVal:
                        elements.append(nums[nextCount])
                        stack.append(elements)
                        totalLength+=1
                    nextCount+=1
                count+=1
            return totalLength




if __name__=="__main__":
    nums=[1,2,3,4]
    print(Solution().numberOfArithmeticSlices(nums=nums))