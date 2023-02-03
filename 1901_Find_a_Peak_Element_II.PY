from typing import List
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        l=0
        h=len(mat)-1
        while l<h:
            m=(l+h)//2
            mMax=max(mat[m])
            mMaxNext=max(mat[m+1])
            if mMax>=mMaxNext:
                h=m
            else:
                l=m+1
        maxM=max(mat[l])
        maxMIndex=mat[l].index(maxM)
        return (l,maxMIndex)
if __name__=="__main__":
    mat=[[1,4],[3,2]]
    print(Solution().findPeakGrid(mat=mat))