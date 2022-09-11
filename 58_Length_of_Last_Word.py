class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last=None
        k=''
        for c in s[::-1]:
            if c and c!=" ":
                k+=c
            else:
                if k:
                    last=k
                    k=""
                    break
        if k:
            last=k
        return len(last)
        
if __name__=="__main__":
    s = "luffy is still joyboy     "
    print(Solution().lengthOfLastWord(s=s))