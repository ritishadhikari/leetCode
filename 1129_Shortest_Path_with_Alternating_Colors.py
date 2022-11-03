# Can Skip
from typing import List
from collections import defaultdict,deque
from math import inf

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph=defaultdict(lambda : defaultdict(lambda: set()))
        
        red=0
        blue=1
        for start, dest in redEdges:
            graph[start][red].add(dest)
        for start, dest in blueEdges:
            graph[start][blue].add(dest)
        
        result=[inf]*n

        q=deque([[0,red],[0,blue]])
        level=-1
        while q:
            size=len(q)
            level+=1
            while size:
                node, color = q.popleft()
                result[node]=min(level, result[node])
                oppColor=color^1
                neighbors=graph[node][oppColor]
                for neighbor in list(neighbors):
                    q.append([ neighbor,oppColor])
                    graph[node][oppColor].remove(neighbor)
                size-=1
        return [res if res is not inf else -1 for res in result]


if __name__=="__main__":
    n=5
    redEdges=[[0,1],[0,3],[1,2],[1,3],[2,3],[2,4],[3,4],[4,1]]
    blueEdges=[[0,1],[1,2],[2,0],[2,3],[3,0],[3,1],[4,0]]
    print(Solution().shortestAlternatingPaths(n=5,redEdges=redEdges,blueEdges=blueEdges))