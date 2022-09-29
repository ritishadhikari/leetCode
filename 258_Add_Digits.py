class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            s=0
            num=str(num)
            for i in num:
                s+=int(i)
            num=s
        return num

if __name__=="__main__":
    num=0
    print(Solution().addDigits(num=num))