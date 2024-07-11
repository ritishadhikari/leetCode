from typing import List

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        sortedScore=sorted(score,key=lambda g:g[k],reverse=True)
        return sortedScore


if __name__=="__main__":
    score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
    k=2
    print(Solution().sortTheStudents(score=score,k=k))