class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels='aeiouAEIOU'
        s=[k for k in s]
        getVowels=[i for i in s if i in vowels]

        index=-1
        for i in range(len(s)):
            if s[i] in vowels:
                s[i]=getVowels[index]
                index-=1

        return ''.join(s)

if __name__=="__main__":
    s = "aA"
    print(Solution().reverseVowels(s=s))