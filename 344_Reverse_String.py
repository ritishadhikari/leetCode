from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # l,r=0,len(s)-1  # l,r are two variables

        # while l<=r:  # total list will be traversed, time complexity will be O(N)
        #     s[l],s[r]=s[r],s[l]
        #     l+=1
        #     r-1

        # Alternate

        toTraverse=len(s)//2

        for i in range(toTraverse):
            s[i],s[-1-i]=s[-1-i],s[i]


if __name__=="__main__":
    s =  ["H","a","n","n","a","h"]
    print(Solution().reverseString(s=s))
    print(s)
