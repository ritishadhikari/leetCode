class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        latinoSplit=sentence.split(sep=" ")
        ans=""
        for ind,word in enumerate(latinoSplit):
            if word[0] in ("a","e","i","o","u","A","E","I","O","U"):
                ans+=" "+word+"ma"+"a"*(ind+1)
            else:
                if len(word)>1:
                    ans+=" "+word[1:]+word[0]+"ma"+"a"*(ind+1)
                else:
                    ans+=" "+word+"ma"+"a"*(ind+1)
        return ans[1:]
    

if __name__=="__main__":
    sentence="Each word consists of lowercase and uppercase letters only"
    print(Solution().toGoatLatin(sentence=sentence))