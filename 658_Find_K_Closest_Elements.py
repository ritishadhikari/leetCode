### VVI
from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=0
        r=len(arr)-k
        while l<r:
            m=(l+r)//2
            if x-arr[m]>arr[m+k]-x:
                l=m+1
            else:
                r=m 
        return arr[l:l+k]


if __name__=="__main__":
    arr=[1,1,1,1,1,1,1,4,4,4,4,5,6]
    k=4
    x=3