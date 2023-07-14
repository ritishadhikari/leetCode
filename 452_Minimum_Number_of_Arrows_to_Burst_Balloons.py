from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count=0
        last=None
        for xs in points:
            if last is None:
                last=xs
            elif xs[0]<=last[-1] and xs[1]<last[-1]:
                last[1]=xs[1]
            else:
                if xs[0]>last[-1]:
                    count+=1
                    last=xs
        return count+1
if __name__=="__main__":
    points = [[1,2],[2,3],[3,4],[4,5]]
    print(Solution().findMinArrowShots(points=points))