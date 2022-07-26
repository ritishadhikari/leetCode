from typing import List
from collections import deque
class Solution:
    def removeElement(self, nums:List[int], val:int) ->int:
        length=len(nums)
        checkList=deque()
        count=0
        for i in range(length):
            if nums[i]==val:
                checkList.append(i)
                count+=1
            else:
                if checkList:
                    nums[checkList.popleft()]=nums[i]
                    checkList.append(i)
        

        return len(nums)-count
if __name__=="__main__":
    nums=[0,1,2,2,3,0,4,2]
    val=2
    print(Solution().removeElement(nums=nums,val=val))