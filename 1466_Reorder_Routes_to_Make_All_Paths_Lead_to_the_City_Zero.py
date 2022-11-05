from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        destKeySourceVal={}
        sourceKeyDestVal={}
        for source,dest in connections:
            if source not in sourceKeyDestVal: sourceKeyDestVal[source]=[]
            sourceKeyDestVal[source].append(dest)

            if dest not in destKeySourceVal: destKeySourceVal[dest]=[]
            destKeySourceVal[dest].append(source)
        
        count=0
        q=set()
        for i in range(n):
            if i in destKeySourceVal or i in sourceKeyDestVal:
                q.add(i)
                while q:
                    val=q.pop()
                    if val in destKeySourceVal:
                        source=destKeySourceVal.pop(val)
                        for s in source:
                            q.add(s)
                            if s==0:    count+=1
                            if s in sourceKeyDestVal and val in sourceKeyDestVal[s]:  
                                sourceKeyDestVal[s].remove(val)
                                if len(sourceKeyDestVal[s])==0: sourceKeyDestVal.pop(s)
                    if val in sourceKeyDestVal:
                        dest=sourceKeyDestVal.pop(val)
                        count+=len(dest)
                        for d in dest:
                            q.add(d)
                            if d in destKeySourceVal and val in destKeySourceVal[d] : 
                                destKeySourceVal[d].remove(val)
                                if len(destKeySourceVal[d])==0: destKeySourceVal.pop(d)
        return count
            
                            

if __name__=="__main__":
    connections = [[0,2],[0,3],[4,1],[4,5],[5,0]]
    n=6
    print(Solution().minReorder(n=6,connections=connections))