def findSafeWays(grid):
    # Write your code here
        rows=len(grid)
        cols=len(grid[0])
        
        # If path to right is permitted than add one path until we reach the last row
        # If path to bottom is permitted don't add one more path
        maxCount=0
        stack=[(0, 0, 1)]
        while stack:
            r, c, count = stack.pop()
            if r==rows-1:  # we have come to the last row, only go right
                if c<cols-1:  # We have not reached the last column
                    if grid[r][c]==1:
                        stack.append((r+1, c+1, count))
                    else:  # we have reached the last row and column
                        maxCount=max(maxCount, count)
            elif r<rows-1:  # we have not reached the last row
                if c<cols-1:  # We have not reached the last column
                    if grid[r][c+1]==1:  # Check if you can go right
                        stack.append((r, c+1, count+1))
                    if grid[r+1][c]==1:  # Check if you can go down
                        stack.append((r+1, c, count+1))
                if c==cols-1: # we have reached the last column
                    if grid[r+1][c]==1:  # Check if you can go down
                        stack.append((r+1, c, count+1))
        return maxCount

if __name__=="__main__":
    print(findSafeWays(grid=[
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]
    ]))