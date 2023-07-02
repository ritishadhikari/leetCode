class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        if (len(s)-s.count("-"))%k!=0:
            first=(len(s)-s.count("-"))%k
            firstDone=False
        else:
            firstDone=True
        appendList=[]
        count=0
        intermittentString=""
        for i,st in enumerate(s):
            if st!="-":
                if not firstDone:
                    intermittentString+=st
                    count+=1
                    if count==first:
                        firstDone=True
                        count=0
                        appendList.append(intermittentString.upper())
                        intermittentString=""
                else:
                    intermittentString+=st
                    count+=1
                    if count==k:
                        count=0
                        appendList.append(intermittentString.upper())
                        intermittentString=""
        return "-".join(appendList)
        
if __name__=="__main__":
    s = "2-5g-3-J"
    k = 2
    print(Solution().licenseKeyFormatting(s=s,k=k))