import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        i=1
        c=0
        while 5**i<=n:
            c+=1
            i+=1

        m=0
        while c:
            m+=n//(5**c)
            c-=1
        return m



if __name__=="__main__":
    n=5
    print(Solution().trailingZeroes(n=n))