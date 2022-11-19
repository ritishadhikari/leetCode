from typing import List
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        td={}
        for s,d in roads:
            if s not in td: td[s]=[]
            td[s].append(d)
            if d not in td: td[d]=[]
            td[d].append(s)
        maxLen=0
        for i in range(n-1):
            for j in range(i+1,n):
                sourceCount,destCount=(0,0)
                if i in td: sourceCount=len(td[i])
                if j in td: destCount=len([d for d in td[j] if d!=i])
                maxLen=max(sourceCount+destCount,maxLen)
        return maxLen

                

if __name__=="__main__":
    n=8
    roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
    print(Solution().maximalNetworkRank(n=n,roads=roads))