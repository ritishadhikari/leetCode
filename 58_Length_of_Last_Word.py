class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=[m for m in s.split() if m]
        return len(s[-1])

if __name__=="__main__":
    s = "   fly me   to   the moon  "
    print(Solution().lengthOfLastWord(s=s))