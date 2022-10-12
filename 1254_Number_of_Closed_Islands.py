from typing import List
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        left,right,top,down=set(),set(),set(),set()
        connection={}
        count=0
        row,col=len(grid),len(grid[0])
        for i in range(row):
            for j in range(col):
                fourWayConnection=0
                if (i and i<row-1) and (j and j<col-1) and not grid[i][j] :
                    if grid[i][j-1]: left.add((i,j)); fourWayConnection+=1
                    else:
                        if (i,j) not in connection: connection[(i,j)]=[(i,j-1)]
                        else:   connection[(i,j)].append((i,j-1))
                    if grid[i][j+1]: right.add((i,j)); fourWayConnection+=1
                    else:
                        if (i,j) not in connection: connection[(i,j)]=[(i,j+1)]
                        else:   connection[(i,j)].append((i,j+1))
                    if grid[i-1][j]: top.add((i,j)); fourWayConnection+=1
                    else:
                        if (i,j) not in connection: connection[(i,j)]=[(i-1,j)]
                        else:   connection[(i,j)].append((i-1,j))
                    if grid[i+1][j]: down.add((i,j)); fourWayConnection+=1
                    else:
                        if (i,j) not in connection: connection[(i,j)]=[(i+1,j)]
                        else:   connection[(i,j)].append((i+1,j))
                if fourWayConnection==4:
                    count+=1
                    if (i,j) in left: left.remove((i,j))
                    if (i,j) in right: right.remove((i,j))
                    if (i,j) in top: top.remove((i,j))
                    if (i,j) in down: down.remove((i,j))
        
        for i in range(row):
            for j in range(col):
                if (i,j) in connection:
                    island=True
                    allsides=set()
                    stack=[(i,j)]
                    while stack:
                        index=stack.pop()
                        if (not index[0] or index[0]==row-1) or (not index[1] or index[1]==col-1):
                            island=False
                        if index in connection:
                            stack.extend(connection[index])
                            stack=list(set(stack))
                            connection.pop(index)
                            if len(allsides)<4:
                                if index in left:   allsides.add('lc'); left.remove(index)
                                if index in right:   allsides.add('rc'); right.remove(index)
                                if index in top:   allsides.add('tc'); top.remove(index)
                                if index in down:   allsides.add('dc'); down.remove(index)
                    if len(allsides)==4 and island:
                        count+=1
        return count
                        
if __name__=="__main__":
    grid=[
        [0,1,0,1,0,0,0,1,1,0,1,1,0,0,1,1,1,0,1,1],
        [0,1,1,0,0,0,0,1,1,1,0,1,0,1,1,0,0,1,0,1],
        [1,1,0,1,0,0,1,1,1,0,0,0,1,0,0,1,0,1,0,0],
        [0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0],
        [1,1,0,0,1,0,0,1,1,0,1,1,0,1,1,1,0,0,1,1],
        [1,1,0,0,0,0,0,1,0,1,1,1,0,1,0,0,0,0,0,1],
        [1,0,1,1,0,1,0,1,0,0,1,0,1,1,1,1,1,0,1,0],
        [1,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1],
        [0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,1,0,0,0],
        [1,1,0,0,0,0,1,1,0,0,0,1,0,0,1,0,1,0,1,1],
        [1,0,0,1,1,1,1,0,1,0,1,1,1,0,0,0,0,1,1,0],
        [1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,0,1,1,1],
        [0,1,1,0,0,1,1,0,0,1,0,1,1,1,1,1,1,0,0,0],
        [1,0,0,0,1,1,0,1,1,1,0,0,1,0,1,1,0,1,0,1]
        ]

    print(Solution().closedIsland(grid=grid))