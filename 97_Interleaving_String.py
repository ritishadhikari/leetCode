# VVI
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1,l2=len(s1),len(s2)
        if l1+l2!=len(s3): 
            return False
        last=set([(0,0)])
        for ch in s3:
            current=set()
            for i,j in last:
                if i<l1 and s1[i]==ch:
                    current.add((i+1,j))
                if j<l2 and s2[j]==ch:
                    current.add((i,j+1))
            if len(current)==0: 
                return False
            last=current
        return True

if __name__=="__main__":
    s1="aabcc"
    s2="dbbca"
    s3="aadbbcbcac"
    print(Solution().isInterleave(s1=s1,s2=s2,s3=s3))