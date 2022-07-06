from typing import List
from collections import deque
class Solution:
    def trap(self, height: List[int]) -> int:
        
        size=len(height)
        
        # Forward Search
        # counter=0
        # maxLimit=0
        # forwardList=[]
        # while counter<size:
        #     maxLimit=max(maxLimit,height[counter])
        #     forwardList.append(maxLimit)
        #     counter+=1
        
        # # Backward Search
        # counter=size-1
        # maxLimit=0
        # backwardList=deque()
        # while counter>=0:
        #     maxLimit=max(maxLimit,height[counter])
        #     backwardList.appendleft(maxLimit)
        #     counter-=1

        # toFill=0
        # for i in range(size):
        #     minVal=min(forwardList[i],backwardList[i])
        #     toFill=toFill+(minVal-height[i])
        # return toFill

        counter=0
        maxLimitForward=0
        maxLimitBackward=0
        forwardList=[]
        backwardList=deque()
        toFill=0
        while counter<size:
            # For Forward Pass
            maxLimitForward=max(maxLimitForward,height[counter])
            forwardList.append(maxLimitForward)

            # For BackwardPass
            backCounter=size-counter-1
            maxLimitBackward=max(maxLimitBackward,height[backCounter])
            backwardList.appendleft(maxLimitBackward)
           
            counter+=1

        toFill=0
        for i in range(size):
            minVal=min(forwardList[i],backwardList[i])
            toFill=toFill+(minVal-height[i])
        return toFill
        




if __name__=="__main__":
    height = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
    print(Solution().trap(height=height))