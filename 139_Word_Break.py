from typing import List
class Solution():
    def wordBreak(self, s:str, wordDict:List[str]):
        dct=set()
        for index in range(len(s)):
            for word in wordDict:
                startLetterPointer=index-len(word)+1
                endLetterPointer=index+1
                if s[startLetterPointer:endLetterPointer]==word:
                    if not startLetterPointer or startLetterPointer-1 in dct:
                        dct.add(endLetterPointer-1)
        return index in dct
            


if __name__=="__main__":
    s="aaaaaaa"
    wordDict= ["aaa", "aaaa"] 
    print(Solution().wordBreak(s=s, wordDict=wordDict))
