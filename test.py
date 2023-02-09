import math
class Solution():
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
            def lcm(x, y):
                return x * y // math.gcd(x, y)
            
            def count_ugly(n, a, b, c, ab, bc, ca, abc):
                answer = n // a + n // b + n // c
                answer -= n // ab + n // bc + n // ca
                answer += n // abc
                return answer
            
            ab, bc, ca = lcm(a, b), lcm(b, c), lcm(c, a)
            abc = lcm(ab, c)
            low = 1
            high = 2 * 10 ** 9
            while low < high:
                mid = low + (high - low) // 2
                if count_ugly(mid, a, b, c, ab, bc, ca, abc) < n:
                    low = mid + 1
                else:
                    high = mid
            return low
if __name__=="__main__":
    n = 3
    a = 2
    b = 3
    c = 5
    print(Solution().nthUglyNumber(a=a,b=b,c=c,n=n))