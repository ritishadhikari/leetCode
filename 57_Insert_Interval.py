from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        temp=[]
        merged=False
        for i in intervals:
            if not merged and i[0]>=newInterval[0]:
                temp.append(newInterval)
                merged=True
            temp.append(i)
        if not merged:
            temp.append(newInterval)
        res=[]
        for i in temp:
            if res and i[0]<=res[-1][-1]:
                res[-1][-1]=max(res[-1][-1],i[-1])
            else:
                res+=[i]

        return res

if __name__=="__main__":
    intervals = [[1,2],[3,5],[5,7],[8,10],[12,16]]
    newInterval = [5,9]
    print(Solution().insert(intervals=intervals, newInterval=newInterval))