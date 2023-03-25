import math
def findPeakPos(numb):
    l=0
    r=len(numb)-1
    while l<r:
        m=(l+r)//2

        if numb[m]<numb[m+1]:  # increasing slope
            l=m+1
        elif numb[m]>numb[m+1]:  # decreasing slope
            r=m
    return l

def findDecreasingSlope(searchNum,numb):
    l=findPeakPos(numb=numb)
    r=len(numb)-1
    while l<=r:
        m=(l+r)//2
        if numb[m]>searchNum:
            l=m+1
        elif numb[m]<searchNum:
            r=m-1
        else:
            return m+1
    return -math.inf

def findIncreasingSlope(searchNum,numb):
    l=0
    r=findPeakPos(numb=numb)
    while l<=r:
        m=(l+r)//2
        if numb[m]>searchNum:
            r=m-1
        elif numb[m]<searchNum:
            l=m+1
        else:
            return m+1
    return -math.inf



if __name__=="__main__":
    num=[1, 3, 5, 7, 9, 6, 4, 2]
    print(findPeakPos(numb=num))
    print(max(findIncreasingSlope(searchNum=8,numb=num),findDecreasingSlope(searchNum=8,numb=num)))