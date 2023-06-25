from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=9
        col=9
        box1,box2,box3,box4,box5,box6,box7,box8,box9=\
            set(),set(),set(),set(),set(),set(),set(),set(),set()
        rw1,rw2,rw3,rw4,rw5,rw6,rw7,rw8,rw9=\
            set(),set(),set(),set(),set(),set(),set(),set(),set()
        cl1,cl2,cl3,cl4,cl5,cl6,cl7,cl8,cl9=\
            set(),set(),set(),set(),set(),set(),set(),set(),set()
        for i,r in enumerate(board):
            for j,c in enumerate(r):
                if c==".":
                    continue
                if i>=0 and i<3:
                    if j>=0 and j<3:
                        if c in box1:   return False
                        else:   box1.add(c)
                    elif j>=3 and j<6:
                        if c in box2:   return False
                        else: box2.add(c)
                    elif j>=6 and j<9:
                        if c in box3:   return False
                        else: box3.add(c)
                elif i>=3 and i<6:
                    if j>=0 and j<3:
                        if c in box4:   return False
                        else:   box4.add(c)
                    elif j>=3 and j<6:
                        if c in box5:   return False
                        else: box5.add(c)
                    elif j>=6 and j<9:
                        if c in box6:   return False
                        else: box6.add(c)
                elif i>=6 and i<9:
                    if j>=0 and j<3:
                        if c in box7:   return False
                        else:   box7.add(c)
                    elif j>=3 and j<6:
                        if c in box8:   return False
                        else: box8.add(c)
                    elif j>=6 and j<9:
                        if c in box9:   return False
                        else: box9.add(c)
                if c in eval(f"rw{i+1}"): return False
                else: eval(f"rw{i+1}").add(c)
                if c in eval(f"cl{j+1}"): return False
                else: eval(f"cl{j+1}").add(c)
        return True

                        


if __name__=="__main__":
    board=[["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(Solution().isValidSudoku(board=board))