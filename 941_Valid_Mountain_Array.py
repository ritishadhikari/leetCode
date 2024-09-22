from typing import List

class Solution:
    def checkNextPattern(self,presentVal, nextVal):
        return True if presentVal>nextVal else False
            
        
    def validMountainArray(self, arr: List[int]) -> bool:
        downwardDetected=False
        upwardDetected=False
        if len(arr)<3: return False
        for i in range(len(arr)-1):
            presentVal,nextVal=arr[i],arr[i+1]
            if presentVal==nextVal:
                return False
            if self.checkNextPattern(presentVal=presentVal,nextVal=nextVal):
                if downwardDetected is False:
                    downwardDetected=True
            else:
                upwardDetected=True
                if downwardDetected:
                    return False
        return True if downwardDetected and upwardDetected else False




if __name__=="__main__":
    arr=[9,8,7,6,5,4,3,2,1,0]
    print(Solution().validMountainArray(arr=arr))