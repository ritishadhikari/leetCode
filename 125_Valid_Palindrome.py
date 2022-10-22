class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=''
        for char in s[::-1]:
            if 65<=ord(char)<=90:
                t+=char.lower()
            elif 48<=ord(char)<=57 or 97<=ord(char)<=122 :
                t+=char
        if t==t[::-1]:  return True
        else: return False

if __name__=="__main__":
    s = "0P"
    print(Solution().isPalindrome(s=s))