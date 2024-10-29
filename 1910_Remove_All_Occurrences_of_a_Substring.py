class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s=s.replace(part,"",1)
        return s

if __name__=="__main__":
    s="abaabcbaabcbcc"
    part="abc"
    print(Solution().removeOccurrences(s=s,part=part))