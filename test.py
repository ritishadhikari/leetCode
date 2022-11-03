from collections import defaultdict, deque
from typing import List
import math
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda : defaultdict(lambda: set()))
        red, blue = 0, 1
        for st, end in red_edges:
            graph[st][red].add(end)
        for st, end in blue_edges:
            graph[st][blue].add(end)
        res = [math.inf] * n
        
        q = deque([(0,red), (0,blue)])
        level = -1
        while q:
            level += 1
            size = len(q)
            for i in range(size):
                node, color = q.popleft()
                opp_color = color^1
                res[node] = min(level, res[node])
                neighbors = graph[node][opp_color]
                for child in list(neighbors):
                    graph[node][opp_color].remove(child)
                    q.append((child, opp_color))
        return [r if r != math.inf else -1 for r in res]

if __name__=="__main__":
    redEdges=[[0,1],[0,3],[1,2],[1,3],[2,3],[2,4],[3,4],[4,1]]
    blueEdges=[[0,1],[1,2],[2,0],[2,3],[3,0],[3,1],[4,0]]
    print(Solution().shortestAlternatingPaths(n=5, 
                    red_edges=redEdges, 
                    blue_edges=blueEdges))