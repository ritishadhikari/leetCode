class Solution:
    def removeDuplicates(self, s: str) -> str:
        uniqueElements=[]
        for i,ch in enumerate(s):
            if uniqueElements:
                if uniqueElements[-1]==ch: uniqueElements.pop()
                else:   uniqueElements.append(ch)
            else:
                uniqueElements.append(ch)
        return ''.join(uniqueElements)

if __name__=="__main__":
    s = "abbaca"
    print(Solution().removeDuplicates(s=s))