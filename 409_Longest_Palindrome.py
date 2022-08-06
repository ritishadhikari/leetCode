class Solution:
    def longestPalindrome(self, s: str) -> int:
        oddChars=set()

        for char in s:
            if char in oddChars:
                oddChars.remove(char)
            else:
                oddChars.add(char)
            
        return len(s)-len(oddChars)+1 if oddChars else len(s)

if __name__=="__main__":
    s = "zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez"
    print(Solution().longestPalindrome(s=s))