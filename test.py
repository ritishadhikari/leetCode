class Solution(object):
    def maxDistance(self, grid):
        s = set()
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    s.add((i, j))
        
        iter = 0
        while s:
            ns = set()
            iter += 1
            
            for cor in s:
                i = cor[0]
                j = cor[1]
                
				#top cell
                if i !=0 and not grid[i-1][j]:
                    grid[i-1][j] = 1
                    ns.add((i-1, j))
                
				#left cell
                if j !=0 and not grid[i][j-1]:
                    grid[i][j-1] = 1
                    ns.add((i, j-1))
                
				#bottom cell
                if i !=n-1 and not grid[i+1][j]:
                    grid[i+1][j] = 1
                    ns.add((i+1, j))
                
				#right cell
                if j != m-1 and not grid[i][j+1]:
                    grid[i][j+1] = 1
                    ns.add((i, j+1))
            s = ns
        
		#ans is iter - 1 because the loop runs for 1 more iteration to make sure no water cells are left.
		
		#if no water cells are present
        if iter-1 == 0:
            return -1
        return iter - 1

if __name__=="__main__":
    grid=[
            [1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,0,0],
            [1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1],
            [0,0,1,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0],
            [0,0,1,1,0,0,0,1,1,1,1,0,1,1,1,0,0,1,0,1],
            [1,0,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0,1,0],
            [0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1],
            [0,0,0,1,0,0,1,1,0,0,1,1,1,1,0,0,0,0,1,0],
            [1,0,0,1,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1],
            [0,1,0,1,1,0,0,1,1,1,1,1,0,0,1,0,1,0,0,0],
            [1,0,1,0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,0],
            [0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0],
            [0,0,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0],
            [0,0,1,1,0,0,1,1,1,1,1,1,1,0,1,0,1,0,0,0],
            [0,1,0,1,0,0,0,1,1,1,0,0,0,1,1,0,0,1,0,1],
            [1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,0,0,0,1,1],
            [0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],
            [0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,0,0,0,1],
            [1,1,1,0,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,0],
            [1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1],
            [0,0,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,0,0]
            ]
    print(Solution().maxDistance(grid=grid))