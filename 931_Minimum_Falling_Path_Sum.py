from typing import List
from math import inf

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        maxCol=len(matrix[0])
        prevDict={i:val for i,val in enumerate(matrix[0])}
        for i in range(len(matrix)-1):
            currentDict={}
            for j in range(maxCol):
                if j==0:
                    lastDiag=None
                else:
                    lastDiag=j-1
                    currentDict[lastDiag]=min(currentDict.get(lastDiag,inf),prevDict[j]+matrix[i+1][lastDiag])
                if j==maxCol-1:
                    nextDiag=None
                else:
                    nextDiag=j+1
                    currentDict[nextDiag]=min(currentDict.get(nextDiag,inf),prevDict[j]+matrix[i+1][nextDiag])
                belowRow=j
                currentDict[belowRow]=min(currentDict.get(belowRow,inf),prevDict[j]+matrix[i+1][belowRow])
            prevDict=currentDict

        return min(prevDict.values())


if __name__=="__main__":
    matrix=[[-48]]
    print(Solution().minFallingPathSum(matrix=matrix))