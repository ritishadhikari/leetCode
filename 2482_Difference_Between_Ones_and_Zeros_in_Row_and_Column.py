from typing import List
from collections import defaultdict
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRowI,onesColJ=defaultdict(lambda:0),defaultdict(lambda:0)
        zerosRowI,zerosColJ=defaultdict(lambda:0),defaultdict(lambda:0)
        rows,cols=len(grid),len(grid[0])
        refGrid=[[0 for j in range(cols)]  for i in range(rows)]
        for row in range(rows):
            for col in range(cols):
                value=grid[row][col]
                if value:
                    onesRowI[row]+=1
                    onesColJ[col]+=1
                else:
                    zerosRowI[row]+=1
                    zerosColJ[col]+=1

        for row in range(rows):
            for col in range(cols):
                refGrid[row][col]=onesRowI[row]+onesColJ[col]-\
                    zerosRowI[row]-zerosColJ[col]
                
        return refGrid


        

if __name__=="__main__":
    grid = [[1,1,1],[1,1,1]]
    print(Solution().onesMinusZeros(grid=grid))
