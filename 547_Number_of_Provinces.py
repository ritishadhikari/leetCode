## VVI
from typing import List
from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected):
        if len(isConnected)==0:
            return 0
        else:
            s=set(range(len(isConnected)))
            count=0
            q=[]
            while True:
                if len(q)==0:
                    if s:
                        q.append(s.pop())
                        count+=1
                    else:
                        break
                item,q=q[0],q[1:]
                for i in list(s):
                    if isConnected[item][i]==1:
                        s.remove(i)
                        q.append(i)
            return count


if __name__=="__main__":
    isConnected = [[1,1,0,0,1],[1,1,0,1,0],[0,0,1,0,0],[0,1,0,1,1],[1,0,0,1,1]]
    print(Solution().findCircleNum(isConnected=isConnected))