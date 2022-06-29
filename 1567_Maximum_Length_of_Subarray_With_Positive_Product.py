from typing import List
class Solution:
    def getMaxLen(self,nums: List[int]) -> int:
        ans=0
        maxPositiveLen=0
        maxNegativeLen=0
        for val in nums:
            if val>0:
                maxPositiveLen=maxPositiveLen+1
                if maxNegativeLen:
                    maxNegativeLen=maxNegativeLen+1
                else:
                    maxNegativeLen=maxNegativeLen
            elif val<0:
                tempVal=maxNegativeLen
                maxNegativeLen=maxPositiveLen+1
                if not tempVal:
                    maxPositiveLen=0
                else:
                    maxPositiveLen=tempVal+1
            elif not val:
                maxPositiveLen=maxNegativeLen=0
            ans=max(ans,maxPositiveLen)
           

        return ans


if __name__=="__main__":
    nums=[-7,-10,-7,21,20,-12,-34,26,2]
    nums=[0,3,1,-2,1,-2,-3,-4]

    {0:{'pos':0,'neg':0},1:{'pos':1,'neg':0},2:{'pos':2,'neg':0},3:{'pos':0,'neg':3},
     4:{'pos':1,'neg':4},5:{'pos':5,'neg':2},6:{'pos':3,'neg':6},7:{'pos':7,'neg':4}}

    nums=[-16,0,-5,2,2,-13,11,8]
    nums=[1,-2,-3,4]
    print(Solution().getMaxLen(nums=nums))