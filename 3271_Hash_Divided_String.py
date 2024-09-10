class Solution:
    def stringHash(self, s: str, k: int) -> str:
        alphabets='abcdefghijklmnopqrstuvwxyz'
        trackerAlp2Digit={a:i for i,a in enumerate(alphabets)}
        trackerDigit2Alphabet={i:a for i,a in enumerate(alphabets)}
        start=0
        result=""
        while start<=len(s)-1:
            substr=s[start:start+k]
            start+=k

            value=sum([trackerAlp2Digit[ind] for ind in substr])%26
            result+=trackerDigit2Alphabet[value]
        return result
if __name__=="__main__":
    s="mxz"
    k=3
    print(Solution().stringHash(s=s,k=k))