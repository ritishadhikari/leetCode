class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        

        for i in range(1,n+1):
            if i==1:
                lst=[1]
            else:
                returnVal=""
                c=0
                past=None
                for l in lst:
                    if past is None:
                        c+=1
                    else:
                        if l==past:
                            c+=1
                        else:
                            returnVal+=str(c)
                            returnVal+=str(past)
                            c=1
                    past=l
                returnVal+=str(c)
                returnVal+=str(past)
                lst=[int(l) for l in returnVal]
        return returnVal


if __name__=="__main__":
    n=4
    print(Solution().countAndSay(n=n))

