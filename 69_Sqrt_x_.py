
class Solution:
    def mySqrt(self, x: int) -> int:
        val=x//2
        high=x
        low=0
        valSet=set()
        while val>=0:
            if val*val==x:
                return val
            elif val*val>x:
                if val in valSet:
                    return val-1
                else:
                    valSet.add(val)
                    high=min(high,val)
                    val=val-((high-low)//2)
                    # val=max(val//2,1)
            elif val*val<x:
                if val in valSet:
                    return val
                else:
                    valSet.add(val)
                    low=max(low,val)
                    val=val+max((high-low)//2,1)
        return val

if __name__=="__main__":
    x=65
    print(Solution().mySqrt(x=x))