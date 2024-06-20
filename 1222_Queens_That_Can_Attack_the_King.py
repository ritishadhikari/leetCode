from typing import List
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        answer=[]
        king=[king]
        for q in queens:
            x,y=q
            if (x,y) in king:
                answer.append(q)
                continue
            else:
                achieved=False
                # Top
                while not achieved and x>=0:
                    x-=1
                    if [x,y] in king:
                        answer.append((q[0],q[1]))
                        achieved=True
                    if [x,y] in queens:
                        break

                # Bottom
                x,y=q
                while not achieved and x<=7:
                    x+=1
                    if [x,y] in king:
                        answer.append((q[0],q[1]))
                        achieved=True
                    if [x,y] in queens:
                        break

                # Left
                x,y=q
                while not achieved and y>=0:
                    y-=1
                    if [x,y] in king:
                        answer.append((q[0],q[1]))
                        achieved=True
                    if [x,y] in queens:
                        break

                # Right
                x,y=q
                while not achieved and y<=7:
                    y+=1
                    if [x,y] in king:
                        answer.append((q[0],q[1]))
                        achieved=True
                    if [x,y] in queens:
                        break

                # Diag left up
                x,y=q
                while not achieved and x>=0 and y>=0:
                    y-=1
                    x-=1
                    if [x,y] in king:
                        answer.append((q[0],q[1]))
                        achieved=True
                    if [x,y] in queens:
                        break

                # Diag right up
                x,y=q
                while not achieved and x>=0 and y<=7:
                    y+=1
                    x-=1
                    if [x,y] in king:
                        answer.append((q[0],q[1]))
                        achieved=True
                    if [x,y] in queens:
                        break

                # Diag left down
                x,y=q
                while not achieved and x<=7 and y>=0:
                    y-=1
                    x+=1
                    if [x,y] in king:
                        answer.append((q[0],q[1]))
                        achieved=True
                    if [x,y] in queens:
                        break

                # Diag right down
                x,y=q
                while not achieved and x<=7 and y<=7:
                    y+=1
                    x+=1
                    if [x,y] in king:
                        answer.append((q[0],q[1]))
                        achieved=True
                    if [x,y] in queens:
                        break
        return answer
    
if __name__=="__main__":
    queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]]
    king=[3,3]
    print(Solution().queensAttacktheKing(queens=queens,
                                         king=king))