from typing import List
import math
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row=len(img)
        col=len(img[0])

        res=[]
        for a in img:
            res.append([0]*len(a))

        for r in range(row):
            for c in range(col):
                firstRow=max(r-1,0)
                lastRow=min(r+2,row)
                firstCol=max(c-1,0)
                lastCol=min(c+2,col)
                
                mat=[subImg[firstCol:lastCol] for subImg in img[firstRow:lastRow]]
                tot=0
                count=0
                for m in mat:
                    count+=len(m)
                    tot+=sum(m)
                
                res[r][c]=math.floor(tot/count)

        return res


if __name__=="__main__":
    img = [[100,200,100],[200,50,200],[100,200,100]]
    print(Solution().imageSmoother(img=img))