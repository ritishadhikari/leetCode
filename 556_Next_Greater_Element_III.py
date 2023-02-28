class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        if n>2**31-1: return -1
        
        strN=str(n)
        numStore=[int(n) for n in strN]
        
        if numStore==sorted(numStore, reverse=True): 
            return -1
        else:
            minElementReplace=max([i for i in range(len(numStore)-1) if numStore[i]<numStore[i+1]])
            maxElementReplace=max([i for i in range(minElementReplace+1,len(numStore)) if numStore[minElementReplace]<numStore[i]])
            
            numStore[minElementReplace],numStore[maxElementReplace]=numStore[maxElementReplace],numStore[minElementReplace]
            numStore[minElementReplace+1:]=sorted(numStore[minElementReplace+1:])

            l=len(numStore)-1
            n=0
            val=0
            while l>=0:
                val+=numStore[l]*10**n
                n+=1
                l-=1


            return int(val) if int(val)<=2**31-1 else -1

if __name__=="__main__":
    n=23541
    print(Solution().nextGreaterElement(n=n))