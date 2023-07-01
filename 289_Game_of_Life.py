from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        trace={}
        row=len(board)
        col=len(board[0])

        for r in range(row):
            for c in range(col):
                trace[(r,c)]=board[r][c]

        for r in range(row):
            for c in range(col):
                live=0
                dead=0
                neighbors=[
                            (r,c-1),(r,c+1),  # left, right
                            (r-1,c),(r+1,c),  # up, down
                            (r-1,c-1),(r-1,c+1),  # dl up, dr up
                            (r+1,c-1),(r+1,c+1)  # dl down, dr down
                            ]
                for n in neighbors:
                        if n[0]>=0 and n[0]<row and n[1]>=0 and n[1]<col:
                            if trace[(n[0],n[1])]==0:
                                dead+=1
                            elif trace[(n[0],n[1])]==1:
                                live+=1
                
                if board[r][c]==1:
                    if live<2 or live>3: 
                        board[r][c]=0

                elif board[r][c]==0:
                    if live==3: 
                        board[r][c]=1
                
if __name__=="__main__":
    board = [[1,1],[1,0]]
    
    print(Solution().gameOfLife(board=board))
    