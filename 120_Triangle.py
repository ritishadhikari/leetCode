from typing import List
from math import inf
class Solution:
    def minimumTotal(self, triangle:List[List[int]]) -> int:
        # previousDict={i:s for i,s in enumerate(triangle[0])}
        # for i in range(len(triangle)-1):
        #     currentDict={}
        #     maxCol=len(triangle[i+1])
        #     for j,val in enumerate(triangle[i]):
        #         if j==maxCol-1: 
        #             nextCol=None
        #         else:
        #             nextCol=j+1
        #             currentDict[nextCol]=min(currentDict.get(nextCol,inf),previousDict[j]+triangle[i+1][nextCol])
        #         belowCol=j
        #         currentDict[belowCol]=min(currentDict.get(belowCol,inf),previousDict[j]+triangle[i+1][belowCol])
        #     previousDict=currentDict
        # return min(previousDict.values())

        previousList=triangle[0]
        for i in range(len(triangle)-1):
            maxCol=len(triangle[i])
            currentList=[inf]*(maxCol+1)
            for j in range(maxCol):
                nextCol=j+1
                currentList[nextCol]=min(currentList[nextCol],previousList[j]+triangle[i+1][nextCol])
                belowCol=j
                currentList[belowCol]=min(currentList[belowCol],previousList[j]+triangle[i+1][belowCol])
            previousList=currentList
        return min(previousList)


if __name__=="__main__":
    triangle=[[2],[3,4],[6,5,7],[4,1,8,3]]
    print(Solution().minimumTotal(triangle=triangle))