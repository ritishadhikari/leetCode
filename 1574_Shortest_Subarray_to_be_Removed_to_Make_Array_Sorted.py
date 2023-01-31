# vvi
from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        arrLen=len(arr)
        i=0
        while i<arrLen-1 and arr[i+1]>=arr[i]:
            i+=1
        if i==arrLen: return 0

        j=arrLen-1
        while j>0 and arr[j]>=arr[j-1]:
            j-=1
        if j==0: return arrLen-1    

        def searchService(endStart,target):
            right=len(arr)-1
            minL=right+1  # or inf # at the most it can go out of the index list
            while endStart<=right:
                m=(endStart+right)//2
                if arr[m]<target:
                    endStart=m+1
                else:
                    right=m-1
                    minL=min(minL,m)
            return minL

        minSubArrLen=min(arrLen-(i+1),j)

        for k in range(i+1):
            subArrEnd=searchService(endStart=j,target=arr[k])
            minSubArrLen=min(minSubArrLen,subArrEnd-(k+1))
        return minSubArrLen



if __name__=="__main__":
    arr = [5,4,3,2,1]
    print(Solution().findLengthOfShortestSubarray(arr=arr))
