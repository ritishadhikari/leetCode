from collections import deque
class Solution:
    def climbStairs(self, n:int) -> int:
        # stack=deque()
        # if n>=2:
        #     stack.append([1])
        #     stack.append([2])
        # else:
        #     stack.append([1])
        
        # count=0
        # while stack:
        #     val=stack.popleft()
        #     diffval=n-sum(val)
        #     if not diffval:
        #         count+=1
        #     elif diffval==1:
        #         stack.append(val+[1])
        #     elif diffval>=2:
        #         stack.append(val+[1])
        #         stack.append(val+[2])
        # return count
        
        sumDict={1:1,2:2}
        if n<3:
            return sumDict[n]
        else:
            count=3
            while count<=n:
                sumDict[count]=sumDict[count-1]+sumDict[count-2]
                count+=1

        return sumDict[n]

if __name__=="__main__":
    stairCount=105
    print(Solution().climbStairs(n=stairCount))