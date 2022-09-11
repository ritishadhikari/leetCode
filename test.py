from typing import List
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        parent = defaultdict(set)
        child = defaultdict(set)
        for i, j in prerequisites:
            parent[i].add(j)
            child[j].add(i)
        bfs = [i for i in range(numCourses) if not parent[i]]
        for i in bfs:
            if parent[i]:
                return []
            for j in child[i]:
                parent[j].remove(i)
                if not parent[j]:
                    bfs += j,
        return bfs if len(bfs)==numCourses else []

if __name__=="__main__":
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(Solution().findOrder(numCourses=4, prerequisites=prerequisites))