class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lst=[i for i in range(1,n+1)]
        pos=0
        length=len(lst)
        while len(lst)>1:
            pos=(pos+(k%length)-1)%length
            lst.pop(pos)
            length-=1
        return lst[0]

if __name__=="__main__":
    n=5
    k=2
    print(Solution().findTheWinner(n=n,k=k))