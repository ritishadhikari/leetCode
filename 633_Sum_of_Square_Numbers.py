import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=math.sqrt(c)
        if int(a)**2==c:
            return True
        else:
            a=int(a)
        rem=int(c-(a**2))
        b=math.sqrt(rem)
        while a>=b:
            if rem%b==0:
                return True
            else:
                a-=1
                rem=int(c-(a**2))
                b=math.sqrt(rem)

if __name__=="__main__":
    c=1000
    print(Solution().judgeSquareSum(c=c))