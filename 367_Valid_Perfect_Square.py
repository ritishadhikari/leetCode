class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=0
        r=num
        m=(l+r)//2
        while l<=r:
            if m*m==num: return True
            elif m*m>num: r=m-1
            else: l=m+1
            m=(l+r)//2
        return False
                

if __name__=="__main__":
    num=16
    print(Solution().isPerfectSquare(num=num))