from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        trace={}
        sidesToExplore=[(-1,0),  # up
                        (1,0),  # down
                        (0,-1),  # left
                        (0,1)]  # right

        rows=len(board)
        cols=len(board[0])

        for r in range(1,rows-1):
            for c in range(1,cols-1):
                if board[r][c]=="O":
                    alone=True
                    for side in sidesToExplore:
                        R,C=r+side[0],c+side[1]
                        if (R>=1 and R<rows-1) and (C>=1 and C<cols-1):
                            if board[R][C]=="O":
                                alone=False
                                if (r,c) not in trace:
                                    trace[(r,c)]=[(R,C)]
                                else:
                                    trace[(r,c)].append((R,C))
        
                    if alone:
                        trace[(r,c)]=[]
        stack=[]
        for r in range(rows):
            for c in range(cols):
                if r!=0 and r!=rows-1 and c!=0 and c!=cols-1:
                    continue
                else:
                    if board[r][c]=="O":
                        for side in sidesToExplore:
                            R,C=r+side[0],c+side[1]
                            if (R>=1 and R<rows-1) and (C>=1 and C<cols-1):
                                if (R,C) in trace:
                                    stack.append((R,C))
                                    while stack:
                                        toRemove=stack.pop()
                                        if toRemove in trace:
                                            stack.extend(trace[toRemove])
                                            trace.pop(toRemove)
        
        keys=trace.keys()
        st=[]
        for (i,j) in list(keys):
            st.append((i,j)) 
            while st:
                makeX=st.pop()
                board[makeX[0]][makeX[1]]="X"
                if makeX in trace:
                    st.extend(trace[makeX])     
                    trace.pop(makeX)

        return board

if __name__=="__main__":

    print(Solution().solve(
        board = 
                [
                    ["O","O","O","O","X","X"],
                    ["O","O","O","O","O","O"],
                    ["O","X","O","X","O","O"],
                    ["O","X","O","O","X","O"],
                    ["O","X","O","X","O","O"],
                    ["O","X","O","O","O","O"]
                ]

                    )
                )
        