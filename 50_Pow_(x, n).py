import math
class Solution:
    def myPow(self, x: float, n: int) -> float:
        result=math.pow(x,n)
        
        return result

if __name__=="__main__":
    x=2.00000
    n=10
    print(Solution().myPow(x=x,n=n))