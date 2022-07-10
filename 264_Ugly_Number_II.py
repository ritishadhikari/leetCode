from numpy import number


class Solution:

    def getPrime(self,number):

        if number in [1,2,3,5]:
            return True

        data=set()
        n=number//2+1
        while n>=2:
            case=None
            if number%n==0 and (n==2 or n%2==1):
                case=True
                p=n//2

                while p>1 and p!=n:
                    if n%p==0:
                        case=False
                        break
                    p-=1
            if case: 
                if n not in [2,3,5]:
                    return False
                else:
                    data.add(n)
            n-=1
        if data:
            return True
        else:
            return False
    
    def nthUglyNumber(self, n:int) ->int:
        maxVal=1
        number=1
        count=1
        while True:
            if maxVal<number and self.getPrime(number=number):
                maxVal=number
                count+=1
            if count==n:
                return maxVal
            number+=1

if __name__=="__main__":
    n=11
    print(Solution().nthUglyNumber(n=n))
