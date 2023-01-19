from typing import List
from math import inf

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        indexedIntervals=[-1]*len(intervals)
        setInterval={tuple(val):ind for ind,val in enumerate(intervals)}
        sortedIntervals=sorted(intervals,key=lambda x:(x[0],x[1]),reverse=False)
        
        def getBestValue(l,index):
            best=inf
            r=len(intervals)-1
            while l<=r:
                m=(l+r)//2
                if sortedIntervals[m][0]>sortedIntervals[index][1]:
                    if best>sortedIntervals[m][0]: 
                        best=sortedIntervals[m][0]
                        bestIndex=sortedIntervals[m]
                        r=m-1
                elif sortedIntervals[m][0]<sortedIntervals[index][1]:
                        l=m+1
                else: return sortedIntervals[m]
            return -1 if best is inf else bestIndex

        for i,num in enumerate(sortedIntervals):
            l=i
            bestValue=getBestValue(l=l,index=i)
            if bestValue==-1: 
                continue
            else:
                indexedIntervals[setInterval[tuple(num)]]=setInterval[tuple(bestValue)]
        
        return indexedIntervals

if __name__=="__main__":
    intervals=[[1,1],[3,4]]
    print(Solution().findRightInterval(intervals=intervals))