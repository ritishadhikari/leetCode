from typing import List
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def isArithmetic(start,stop):
            arr=nums[start:stop+1]
            arr.sort()

            if len(arr)==1: return True

            d=None
            for i,v in enumerate(arr):
                if i and d is None:
                    d=arr[i]-arr[i-1]
                elif i and d is not None and d!=arr[i]-arr[i-1]: return False

            return True
        
        answer=[]
        
        for s,t in zip(l,r):
            answer.append(True) if isArithmetic(start=s,stop=t) else answer.append(False)
        return answer

if __name__=="__main__":
    nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
    l = [0,1,6,4,8,7]
    r = [4,4,9,7,9,10]
    print(Solution().checkArithmeticSubarrays(nums=nums,l=l,r=r))