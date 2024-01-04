from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # first check whether all the words are present or not
        allChars={}
        for k in board:
            for s in k:
                if s not in allChars:
                    allChars[s]=1
                else:
                    allChars[s]+=1
        # allChars={s for k in board for s in k }
        for c in word:
            if c not in allChars:
                return False
            else:
                allChars[c]-=1
                if allChars[c]==0:
                    allChars.pop(c)

        
        # Fill the position of the first word in a stack
        stack=[]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]==word[0]:
                    stack.append((r,c,0,{(r,c)}))
        
        # Now for each start index follow the remaining words by capturing the 
        # details of the of the following words through its index
        dir=((-1,0),(1,0),(0,-1),(0,1))
        while stack:
            row,col,index,visited=stack.pop()
            if index==len(word)-1: 
                return True
            for r1,c1 in dir:
                R=r1+row
                C=c1+col
                if R>=0 and R<len(board) and C>=0 and C<len(board[0]):
                    if board[R][C]==word[index+1] and (R,C) not in visited:
                        # This step is mandatory because for each new addition, 
                        # the reference index will be added for that
                        # addition only and not added to visit directly
                        # which will carry forward the sequence for this 
                        # index to its other sequence if found in the
                        # dir for the subsequent indexes
                        # newVisited=visited.copy()
                        # newVisited.add((R,C))
                        # stack.append((R,C,index+1,newVisited))

                        stack.append((R,C,index+1,set(list(visited)+[(R,C)])))
        return False

if __name__=="__main__":
    # board = [["A","B","C","E"],
    #          ["S","F","C","S"],
    #          ["A","D","E","E"]]
    # word="ABCB"
    
    board=[
        ["A","B","C","E"],
        ["S","F","E","S"],
        ["A","D","E","E"]]

    word = "ABCESEEEFS" # "CFDE"
    print(Solution().exist(board=board,word=word))
    