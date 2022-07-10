from numpy import number


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        indMul2=0
        indMul3=0
        indMul5=0
        m=[]
        for i in range(n):
            if not m:
                m.append(1)
            else:
                nextMin=min(m[indMul2]*2,m[indMul3]*3,m[indMul5]*5)
                m.append(nextMin)
                if m[indMul2]*2==nextMin:
                    indMul2+=1
                if m[indMul3]*3==nextMin:
                    indMul3+=1
                if m[indMul5]*5==nextMin:
                    indMul5+=1
        return m[-1]

if __name__=="__main__":
    n=11
    print(Solution().nthUglyNumber(n=n))
