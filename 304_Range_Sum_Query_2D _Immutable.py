from typing import List
class NumMatrix:

    def __init__(self,matrix:List[List[int]]):
        self.zeroMat=[[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                valueToAdd=matrix[i][j]
                addFromLeft=self.zeroMat[i+1][j]
                addFromTop=self.zeroMat[i][j+1]
                subtractCommon=self.zeroMat[i][j]
                self.zeroMat[i+1][j+1]=valueToAdd+addFromLeft+addFromTop-subtractCommon

    def sumRegion(self, row1:int, col1:int, row2:int, col2:int) -> int:
        grossValue=self.zeroMat[row2+1][col2+1]
        subtractAbove=self.zeroMat[row1][col2+1]
        subtractLeft=self.zeroMat[row2+1][col1]
        addCommon=self.zeroMat[row1][col1]
        value=grossValue-subtractAbove-subtractLeft+addCommon
        return value
if __name__=="__main__":
    matrix=[[2,4,2],[3,2,3],[3,2,1]]


    obj = NumMatrix(matrix)
    print(obj.zeroMat)
    print(obj.sumRegion(row1=1,col1=1,row2=2,col2=2))
    
