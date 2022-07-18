from typing import List
from collections import deque
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        prevList=deque()
        for i,val in enumerate(grid[0]):
            if not i:
                prevList.append(val)
            else:
                prevList.append(val+prevList[-1])
        
        for i in range(1,len(grid)):
            presentList=deque()
            for j in range(len(grid[0])):
                topValAdd=grid[i][j]+prevList[j]
                if not j:
                    presentList.append(grid[i][j]+prevList[j])
                else:
                    leftValAdd=grid[i][j]+presentList[-1]
                    presentList.append(min(topValAdd,leftValAdd))
            prevList=presentList

        return prevList[-1]

if __name__=="__main__":
    grid = [[1,2,3],[4,5,6]]
    print(Solution().minPathSum(grid=grid))