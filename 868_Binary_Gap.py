from math import inf
class Solution:
    def binaryGap(self, n: int) -> int:
        pos=None
        nBin=str(bin(n)).replace("0b","")
        for i,num in enumerate(nBin):
            if num=="1":
                if pos is None:
                    pos=i
                    diff=0
                else:
                    diff=max(diff,i-pos)
                    pos=i
        return diff
                
        
        

if  __name__=="__main__":
    n=8
    print(Solution().binaryGap(n=n))