from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        elif set(word1)!=set(word2):
            return False
        else:  # this part is tricky
            return Counter(Counter(word1).values())\
                ==Counter(Counter(word2).values())
            

if __name__=="__main__":
    word1 = "cabbba"
    word2 = "abacaa"
    print(Solution().closeStrings(word1=word1, word2=word2))