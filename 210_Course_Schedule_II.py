from typing import List
from collections import defaultdict 

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        parentDict=defaultdict(lambda: set())
        childDict=defaultdict(lambda : set())
        for i,j in prerequisites:
            parentDict[i].add(j)
            childDict[j].add(i)

        search=[i for i in range(numCourses) if i not in parentDict]
        answer=search.copy()
        while search:
            i=search.pop(0)
            childElements=childDict[i]
            for j in childElements:
                parentDict[j].remove(i)
                if not parentDict[j]:
                    answer.append(j)
                    search.append(j)

        return answer if len(answer)==numCourses else []

        for i in search:
            childElements=childDict[i]
            for j in childElements:
                parentDict[j].remove(i)
                if not parentDict[j]:
                    '''
                    If there lies an existing parent, 
                    then do not add to the search list, 
                    else add to the search list
                    '''
                    search.append(j)

        return search if len(search)==numCourses else []
if __name__=="__main__":
    numCourses=2
    prerequisites=[[1,0]]
    print(Solution().findOrder(numCourses=numCourses,
                            prerequisites=prerequisites))