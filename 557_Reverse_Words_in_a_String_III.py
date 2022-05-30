class Solution:
    def reverseWords(self, s: str) -> str:
        
        return " ".join([i[::-1] for i in s.split(" ")])  # Ritish's Solution

        # Method 2 -- Very Slow
        # slist=[0]*len(s)
        # start=0
        # for i,c in enumerate(s):
        #     if c==" ":
        #         count=0
        #         for j in range(start,i):
        #             slist[j]=s[i-count-1]
        #             count+=1
        #         slist[i]=s[i]
        #         start=i+1
        
        # count=1
        # for i in range(start,len(s)):
        #     slist[i]=s[len(s)-count]
        #     count+=1
        # return "".join(slist)

  
        
            




if __name__=="__main__":
    s = "Let's take LeetCode contest"
    print(Solution().reverseWords(s=s))


# 8   14-1
# 9   14-2
# 10  14-3
# 11  14-4
# 12  14-5
# 13  14-6
