import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr=str(x)
        length=math.ceil(len(xstr)/2)
        for i in range(length):
            if xstr[i]!=xstr[-i-1]:
                return False
        return True

if __name__=="__main__":
    print(Solution().isPalindrome(x=-121))