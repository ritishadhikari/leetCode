from typing import List
from collections import defaultdict
from heapq import heappush, heappop
class Solution():
    def diagonalSort(self, A: List[List[int]]) -> List[List[int]]:
            n, m = len(A), len(A[0])
            d = defaultdict(list)
            for i in range(n):
                for j in range(m):
                    heappush(d[i - j], A[i][j])
            for i in range(n):
                for j in range(m):
                    A[i][j] = heappop(d[i - j])
            return A

if __name__=="__main__":
     mat = [
          [11,25,66,1,69,7],
          [23,55,17,45,15,52],
          [75,31,36,44,58,8],
          [22,27,33,25,68,4],
          [84,28,14,11,5,50]
          ]
     print(Solution().diagonalSort(A=mat))