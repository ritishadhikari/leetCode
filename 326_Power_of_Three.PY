class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0: return False
        while n>=1:
            if n==1: return True
            else:
                div=n//3
                mul=div*3
                if n!=mul: 
                    return False
                else: 
                    n=div 
        return True

if __name__=="__main__":
    n=14
    print(Solution().isPowerOfThree(n=n))