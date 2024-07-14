from typing import List
from math import inf
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxSum=-inf
        for i in range(2,len(grid)):
            for j in range(2,len(grid[0])):
                tempSum=grid[i-2][j-2]+grid[i-2][j-1]+grid[i-2][j]+\
                grid[i-1][j-1]+\
                grid[i][j-2]+grid[i][j-1]+grid[i][j]
                maxSum=max(maxSum,tempSum)
        return maxSum

if __name__=="__main__":
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    print(Solution().maxSum(grid=grid))