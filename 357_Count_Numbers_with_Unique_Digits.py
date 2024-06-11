# Can Skip
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        else:
            total=10
            start=9
            for i in range(1,n):
                start*=(10-i)
                total+=start
            return total
if __name__=="__main__":
    n=2
    print(Solution().countNumbersWithUniqueDigits(n=n))