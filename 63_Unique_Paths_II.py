from typing import List
import math
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        evalMat=[[0 for j in range(len(obstacleGrid[0])+1)] for i in range(len(obstacleGrid)+1)]

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                
                if obstacleGrid[i][j]==1:
                    evalMat[i+1][j+1]=0
                else:
                    # CarrySum
                    if not i and not j:
                        addidiveFactor=1
                    else:
                        addFromLeft=evalMat[i+1][j]/2
                        addFromTop=evalMat[i][j+1]/2
                        if i==len(obstacleGrid)-1 or obstacleGrid[i+1][j-1]==1:
                            addFromLeft=evalMat[i+1][j]
                        if j==len(obstacleGrid[0])-1 or obstacleGrid[i-1][j+1]==1:
                            addFromTop=evalMat[i][j+1]
                        addidiveFactor=math.ceil(addFromLeft+addFromTop)
                    
                    # MultiplyPaths
                    if i==len(obstacleGrid)-1 and j==len(obstacleGrid[0])-1:
                        multiplicativeFactor=1
                    else:
                        if i==len(obstacleGrid)-1:
                            addFromDown=0
                        else:
                            if obstacleGrid[i+1][j]==1:
                                addFromDown=0
                            else:
                                addFromDown=1
                        if j==len(obstacleGrid[0])-1:
                            addFromRight=0
                        else:
                            if obstacleGrid[i][j+1]==1:
                                addFromRight=0
                            else:
                                addFromRight=1
                        multiplicativeFactor=math.ceil(addFromDown+addFromRight)
                    evalMat[i+1][j+1]=addidiveFactor*multiplicativeFactor


        return evalMat[-1][-1]

if __name__=="__main__":
    grid=[[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]
    print(Solution().uniquePathsWithObstacles(obstacleGrid=grid))