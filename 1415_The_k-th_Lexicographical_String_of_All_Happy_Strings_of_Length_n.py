class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # {1:3,2:6,3:12,4:24}
        # "3*2^(n-1)"
        if k>3*2**(n-1): 
            return ""
        else:
            tracker={
                'a':['b','c'],
                'b':['a','c'],
                'c':['a','b']
                     }
            queue=['a','b','c']
            while len(queue[0])<n:
                element=queue.pop(0)  # pop from left
                for string in tracker[element[-1]]:
                    queue.append(element+string)  # append from right
            return queue[k-1]

if __name__=="__main__":
    n=3
    k=9
    print(Solution().getHappyString(n=3,k=9))