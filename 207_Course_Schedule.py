# Can Skip
from typing import List
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        origin=[[] for i in range(numCourses)]
        destination=[0]*numCourses
        notaDest=deque()
        travelled=0

        for d,o in prerequisites:
            origin[o].append(d)
            destination[d]+=1
        
        for i, d in enumerate(destination):
            if d==0:
                notaDest.append(i)


        while notaDest:
            lastNode=notaDest.popleft()
            travelled+=1
            for dest in origin[lastNode]:
                destination[dest]-=1
                if destination[dest]==0:
                    notaDest.append(dest)
        
        return travelled==numCourses
                 

if __name__=="__main__":
    numCourses=2
    prerequisites=[[1,0],[0,1]]
    print(Solution().canFinish(numCourses=numCourses, 
                               prerequisites=prerequisites))