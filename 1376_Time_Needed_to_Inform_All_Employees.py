from typing import List
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        traceEmp={}
        for i,v in enumerate(manager):
            if v not in traceEmp:   traceEmp[v]=set()
            traceEmp[v].add(i)
        
        maxTime=0
        stack=set()
        stack.add((headID,informTime[headID]))
        while stack:
            parent,time=stack.pop()
            if informTime[parent]!=0:
                for employee in traceEmp[parent]:
                    stack.add((employee,informTime[employee]+time))
            else:
                maxTime=max(time,maxTime)
        return maxTime





if __name__=="__main__":
    manager=[2,0,-1,4,2,0,4,5,6]
    informTime=[2,0,4,0,3,4,2,0,0]
    headID=2
    print(Solution().numOfMinutes(n=9,headID=headID,
                    manager=manager,informTime=informTime))