class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        result, lastMatch = 0, -1
        for i,element in enumerate(s):
            if element in dic and lastMatch<dic[element]:
                lastMatch=dic[element]
            else:
                result=max(result,(i-lastMatch))
            dic[element]=i

        return result

if __name__=="__main__":
    print(Solution().lengthOfLongestSubstring(s="abbac"))