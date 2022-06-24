from typing import List
class Solution():
    def rob(self, nums: List[int]):
        if len(nums)<=2:
            return max(nums)
        else:
            sizeofArray=len(nums)
            indexes=[(0,sizeofArray-1),(1,sizeofArray)]
            sumVal=0
            for index in indexes:
                prevRobAmount=0
                maxRobAmount=0
                for i in range(index[0],index[1]):
                    tempVal=maxRobAmount
                    maxRobAmount=max(prevRobAmount+nums[i],maxRobAmount)
                    prevRobAmount=tempVal
                sumVal=max(sumVal,maxRobAmount)
            return sumVal

if __name__=="__main__":
    nums=[1,2,3,4,5,1,2,3,4,5]
    print(Solution().rob(nums=nums))
    