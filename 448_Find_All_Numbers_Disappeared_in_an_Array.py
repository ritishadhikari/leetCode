from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        arrLen=len(nums)
        uniqueVals=set(nums)
        result=[]
        for i in range(1,arrLen+1):
            if i not in uniqueVals:
                result.append(i)
        return result


        for i in range(len(nums)):
            absNum=abs(nums[i])
            index=absNum-1
            if nums[index]>0:
                nums[index]=nums[index]*-1
        lst=[]
        for ind, num in enumerate(nums):
            if num>0:
                lst.append(ind+1)

        return lst
    
      
        
    

if __name__=="__main__":
    nums=[1,1]
    print(Solution().findDisappearedNumbers(nums=nums))