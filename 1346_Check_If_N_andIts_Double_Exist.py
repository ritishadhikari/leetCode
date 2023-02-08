from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        trace={}
        for a,i in enumerate(arr):
            if i==0: 
                if 0 not in trace: trace[i]=[a]
                else: trace[i].append(a)
            else: trace[i]=a

        for n in arr:
            if n:
                # half case
                if n%2==0:  # n is even
                    half=n/2
                    if half in trace and trace[n]!=trace[half]: return True
                
                # double case
                double=n*2
                if double in trace and trace[n]!=trace[double]: return True
            else:
                if len(trace[n])>1: return True
        return False

if __name__=="__main__":
    arr=[0,0]
    print(Solution().checkIfExist(arr=arr))