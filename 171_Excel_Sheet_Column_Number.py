class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        s=0
        pow=0
        for ch in columnTitle[::-1]:
            mul=ord(ch)-64
            s+=mul*26**pow
            pow+=1
        return s



if __name__=="__main__":
    columnTitle = "ZBG"
    print(Solution().titleToNumber(columnTitle=columnTitle))