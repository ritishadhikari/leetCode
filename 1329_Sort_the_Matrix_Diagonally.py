from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        tracker=defaultdict(list)
        row,col=len(mat),len(mat[0])

        for r in range(row):
            for c in range(col):
                index=r-c
                heappush(tracker[index],mat[r][c])
        
        for r1 in range(row):
            for c1 in range(col):
                index=r1-c1
                mat[r1][c1]=heappop(tracker[index])
        
        return mat
    
        

if __name__=="__main__":
    mat = [
        [11,25,66,1,69,7],
        [23,55,17,45,15,52],
        [75,31,36,44,58,8],
        [22,27,33,25,68,4],
        [84,28,14,11,5,50]
        ]
    print(Solution().diagonalSort(mat=mat))