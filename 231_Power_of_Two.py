class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        else:
            while n:
                if n==1:
                    return True
                elif n%2==1:
                    return False
                n=n//2


if __name__=="__main__":
    print(Solution().isPowerOfTwo(n=-16))