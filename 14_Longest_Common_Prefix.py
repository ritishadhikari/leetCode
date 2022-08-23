from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallestLength=min(len(v) for v in strs)

        finalString=""
        for i in range(smallestLength):
            letter=strs[0][i]
            discrepancy=False
            for let in strs[1:]:
                if let[i]!=letter:
                    discrepancy=True
                    break
            if discrepancy:
                return finalString
            else:
                finalString+=letter
        return finalString

if __name__=="__main__":
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs=strs))