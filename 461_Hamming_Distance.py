class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        xlst=[]
        while x:
            q=x//2
            r=x%2
            xlst.append(r)
            x=q
        x=(''.join([str(l) for l in xlst[::-1]]))

        ylst=[]
        while y:
            q=y//2
            r=y%2
            ylst.append(r)
            y=q
        y=(''.join([str(l) for l in ylst[::-1]]))
        
        count=0
        if len(x)>len(y):
            diffL=len(x)-len(y)
            y='0'*diffL+y
        elif len(y)>len(x):
            diffL=len(y)-len(x)
            x='0'*diffL+x

        for i in range(len(x)):
            if x[i]!=y[i]:
                count+=1

        return count



if __name__=="__main__":
    x=3
    y=1
    print(Solution().hammingDistance(x=x,y=y))