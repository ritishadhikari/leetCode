class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for j,s in enumerate(haystack):
            if s==needle[0] and haystack[j:j+len(needle)]==needle:
                return j
        return -1


if __name__=="__main__":
    haystack = "mississippi"
    needle = "issip"
    print(Solution().strStr(haystack=haystack,needle=needle))