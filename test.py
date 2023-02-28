class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        if digits == sorted(digits, reverse=True):
            return -1
        
        x = max(i for i in range(len(digits)-1) if digits[i] < digits[i+1])
        y = max(i for i in range(x+1, len(digits)) if digits[i] > digits[x])
        
        digits[x], digits[y] = digits[y], digits[x]
        digits[x+1:] = sorted(digits[x+1:])
        
        nxt = int(''.join(digits))
        
        return nxt if nxt < 2**31 else -1
    
if __name__=="__main__":
    n=158638

    print(Solution().nextGreaterElement(n=n))