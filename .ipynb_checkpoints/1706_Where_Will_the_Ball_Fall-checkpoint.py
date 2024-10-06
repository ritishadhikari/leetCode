from typing import List
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        answer=[]
        rows,cols=len(grid),len(grid[0])
        for col in range(cols):
            c=col
            r=0
            while r<rows:
                if grid[r][c]==1 and c+1<cols and grid[r][c+1]==1:
                    c+=1
                elif grid[r][c]==-1 and c-1>=0 and grid[r][c-1]==-1:
                    c-=1     
                else:
                    answer.append(-1)
                    break
                r+=1
            if r==rows:
                answer.append(c)      
        return answer  

if __name__=="__main__":
     grid = [
         [1,1,1,-1,-1],
         [1,1,1,-1,-1],
         [-1,-1,-1,1,1],
         [1,1,1,1,-1],
         [-1,-1,-1,-1,-1]]
     print(Solution().findBall(grid=grid))