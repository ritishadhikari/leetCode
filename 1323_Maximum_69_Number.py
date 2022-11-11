class Solution:
    def maximum69Number (self, num: int) -> int:
        num=str(num)

        done=False
        changedNum=""
        for n in num:
            if n=="6" and not done:
                n="9"
                done=True
            changedNum+=n
        return int(changedNum)

if __name__=="__main__":
    num = 9669
    print(Solution().maximum69Number(num=num))