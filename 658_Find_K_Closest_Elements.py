### VVI
from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=0
        r=len(arr)-k-1
        while l<=r:
            m=(l+r)//2
            if x-arr[m]>arr[m+k]-x:
                l=m+1
            else:
                r=m-1 
        return arr[l:l+k]


if __name__=="__main__":
    arr=[1,1,1,1,1,1,1,4,4,4,4,5,6]
    arr=[-14,-11,-10,-2,1,1,1,4,4,4,5,6]
    k=4
    x=-1
    # arr=[1,2,3,4,5]
    # k=4
    # x=3
    print(Solution().findClosestElements(arr=arr,k=k,x=x))