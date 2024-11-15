class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            x=int(str(x)[1:][::-1])*-1
            return 0 if x<-2**31 else x
        else:
            x=int(str(x)[::-1])
            return 0 if x>2**31-1 else x
               

if __name__=="__main__":
    x=-2147483648
    print(Solution().reverse(x=x))