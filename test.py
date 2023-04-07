from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Edge case: character in word does not exist in board
        for c in word:
            if c not in set().union(*[set(row) for row in board]):
                return False        
        
        # Initialize DFS stack. Item = (curr x, curr y, letters so far, visited set)
        stack = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    stack.append((i, j, 1, {(i, j)}))
                    
        # DFS
        while stack:
            x, y, ct, visited = stack.pop()
            
            # Solution found
            if ct == len(word):
                return True
            
            # Check up, down, left, right neighbors
            for newX, newY in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= newX and newX < len(board) and 0 <= newY and newY < len(board[0]):
                    if board[newX][newY] == word[ct] and (newX, newY) not in visited:
                        # If neighbor is in range and matches next letter and not visited,
                        # Add neighbor onto visited and add onto stack
                        newVisited = set(visited)
                        newVisited.add((newX, newY))
                        stack.append((newX, newY, ct + 1, newVisited))
                        
        # No solution found
        return False
    

if __name__=="__main__":
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
        ]
    
    board=[
            ["C","B","C"],
            ["C","D","C"],
            ["B","B","D"]
        ]
    word = "BCCB"
    print(Solution().exist(board=board,word=word))