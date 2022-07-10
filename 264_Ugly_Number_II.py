from numpy import number


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        mul2=0
        mul3=0
        mul5=0
        m=[]
        for i in range(n):
            if not m:
                m.append(1)
            else:
                nextMin=min(m[mul2]*2,m[mul3]*3,m[mul5]*5)
                m.append(nextMin)
                if m[mul2]*2==nextMin:
                    mul2+=1
                if m[mul3]*3==nextMin:
                    mul3+=1
                if m[mul5]*5==nextMin:
                    mul5+=1

        return m[-1]

if __name__=="__main__":
    n=11
    print(Solution().nthUglyNumber(n=n))
