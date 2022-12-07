from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l=0
        r=len(letters)-1

        if ord(target)<ord(letters[l]) or ord(target)>=ord(letters[r]) :
            return letters[l]   
        else:
            while l<=r:
                m=(l+r)//2
                if ord(target)<ord(letters[m]):
                    r=m-1
                elif ord(target)>=ord(letters[m]):
                    l=m+1
            return letters[l]

if __name__=="__main__":
    letters = ['a','b','c','c','e','f','f','f','g','g','h','i','j']
    target="d"
    print(Solution().nextGreatestLetter(letters=letters, target=target))