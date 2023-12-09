from typing import List
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        valid=lambda r,c: True if r>=0 and r<rows and c>=0 and c<cols else False
        ret=[(rStart,cStart)]
        steps=1
        while len(ret)<=rows*cols:
            # go east
            for _ in range(steps):
                cStart+=1
                if valid(r=rStart,c=cStart):
                    ret.append((rStart,cStart))
            # go south
            for _ in range(steps):
                rStart+=1
                if valid(r=rStart,c=cStart):
                    ret.append((rStart,cStart))
            steps+=1

            # go west
            for _ in range(steps):
                cStart-=1
                if valid(r=rStart,c=cStart):
                    ret.append((rStart,cStart))
            
            # go north
            for _ in range(steps):
                rStart-=1
                if valid(r=rStart,c=cStart):
                    ret.append((rStart,cStart))
            steps+=1
            
            if len(ret)==rows*cols: break

        return ret


if __name__=="__main__":
    rows=5
    cols=6
    rStart=1
    cStart=4
    print(Solution().spiralMatrixIII(rows=rows,
                                     cols=cols,
                                     rStart=rStart,
                                     cStart=cStart))