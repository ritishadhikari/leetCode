def guess(num: int) -> int:
        k=1
        if num==k:
            return 0
        if num>k:
            return -1
        else:
            return 1
class Solution:
    def guessNumber(self, n: int) -> int:
        l=0
        m=(n+l)//2
        while guess(num=m)==1 or guess(num=m)==-1:
            if guess(num=m)==-1:  # Input Number is higher
                n=m-1 
            elif guess(num=m)==1:  # Input Number is lower
                l=m+1
            m=(n+l)//2
        return m
        
if __name__=="__main__":
    n=10
    print(Solution().guessNumber(n=n))



'''
8
3

8+3//2

'''