from typing import List
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points)==0: 
            return []
        elif len(points)<k: 
            return points 
        else:
            argument=lambda k: math.sqrt(k[0]**2-0+k[1]**2)
            points=sorted(points,key=argument)
            return points[:k]

        

if __name__=="__main__":
    points = [[1,3],[-2,2]]
    k=1
    print(Solution().kClosest(points=points,k=k))