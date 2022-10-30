from re import I


class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        while i<n:
            n-=i 
            i+=1
        return i if i==n else i-1


if __name__=="__main__":
    n=1
    print(Solution().arrangeCoins(n=n))

