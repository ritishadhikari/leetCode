class Solution:
    def isHappy(self, n: int) -> bool:
        
        dct=set()

        while n:
            newN=0
            for l in str(n):
                newN=newN+int(l)**2
            if newN==1:
                return True
            elif newN in dct :
                return False
            else:
                dct.add(newN)
            n=newN 


if __name__=="__main__":
    n = 2
    print(Solution().isHappy(n=n))