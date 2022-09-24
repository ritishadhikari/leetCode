from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals, key=lambda k :k[0])
        res=[]
        for i in intervals:
            if res and res[-1][-1]>=i[0]:
                res[-1][-1]=max(i[-1],res[-1][-1])
            else:
                res.append(i)
        return res

if __name__=="__main__":
    intervals = [[1,4],[4,5]]
    print(Solution().merge(intervals=intervals))