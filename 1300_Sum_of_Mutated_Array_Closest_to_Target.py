from typing import List
from math import inf
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        l=0
        r=max(arr)
        best=l

        def valid(num):
            tot=0
            for v in arr:
                if v<num:tot+=v
                else: tot+=num
            
            if tot>target: return tot-target
            else: return tot-target

        res=inf
        while l<=r:
            m=(l+r)//2
            output=valid(num=m)
            if output>0:
                if abs(output)<res:
                    res=abs(output)
                    best=m
                r=m-1
            elif output<0:
                if abs(output)<=res:
                    res=abs(output)
                    best=m
                l=m+1
            else:
                return m
        return best
                
if __name__=="__main__":
    arr = [60864,25176,27249,21296,20204]
    target = 56803
    print(Solution().findBestValue(arr=arr,target=target))