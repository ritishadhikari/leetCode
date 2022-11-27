from typing import List
import math

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

            if len(arr)<3: return -1
            l=0
            m=math.floor((len(arr)-1)/2)
            r=len(arr)-1

            while m!=l or r!=m:
                if arr[l]<=arr[m] and arr[r]<=arr[m]:
                    incrementalL=(m-l)/2
                    if incrementalL>=1:  l=l+math.floor(incrementalL)
                    else:   l=m

                    decrementalR=(r-m)/2
                    if decrementalR>=1:  r=r-math.floor(decrementalR)
                    else: r=m
                    
                elif arr[r]>arr[m]:
                    m=r
                    r=len(arr)-1
                elif arr[l]>arr[m]:
                    m=l
                    l=0
            
            return m

if __name__=="__main__":
    arr=[0,10,5,2]

    print(Solution().peakIndexInMountainArray(arr=arr))