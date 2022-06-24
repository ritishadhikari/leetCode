from typing import List
import collections 

class Solution(object):
    def deleteAndEarn(self, nums):
        countDict=collections.Counter(nums)
        sortedList=sorted(countDict.keys())
        prev=0
        currentMax=countDict[sortedList[0]]*sortedList[0]
        for i in range(1,len(sortedList)):
            tempVal=currentMax
            if sortedList[i]-sortedList[i-1]==1:
                currentMax=max(currentMax,prev+countDict[sortedList[i]]*sortedList[i])
            else:
                currentMax=currentMax+countDict[sortedList[i]]*sortedList[i]
            prev=tempVal
        return currentMax

if __name__=="__main__":
    nums=[2,2,3,3,3,4,5,5]
    # nums=[3,4,2]
    # nums=[2,2,3,3,3,4]
    # nums=[1]
    # nums=[8,10,4,9,1,3,5,9,4,10]
    # nums=[12,32,93,17,100,72,40,71,37,92,58]
    print(Solution().deleteAndEarn(nums=nums))

    