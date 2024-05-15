class Solution:
    def frequencySort(self, s: str) -> str:
        tracker={}
        ans=''
        for string in s:
            if string not in tracker:
                tracker[string]=1
            else:
                tracker[string]+=1
        tracker=sorted(tracker.items(),
               key=lambda s: s[1],
               reverse=True)
        
        for string,count in tracker:
            ans+=string*count
        return ans



if __name__=="__main__":
    s="Aabb"  
    print(Solution().frequencySort(s=s))