from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        initial=[[i for i in range(1,k+1)]]
        if sum(initial[0])==n :
            return initial
        elif sum([9]*k)==n:
            return [[9]*k]
        elif sum([9]*k)<n:
            return []
        else:
            seen=set()
            answer=[]
            while initial:
                length=len(initial)
                for j in range(length):
                    number=initial.pop(0)
                    for l in range(k):
                        potentialNumber=number.copy()
                        if potentialNumber[l]+1<10:
                            potentialNumber[l]+=1
                            potentialNumber=set(potentialNumber)
                            if len(potentialNumber)==k:
                                if (sum(potentialNumber)==n):
                                    if tuple(sorted(potentialNumber)) not in seen:
                                        seen.add(tuple(sorted(potentialNumber)))
                                        answer.append(list(potentialNumber))
                                elif (sum(potentialNumber)<=n) and list(potentialNumber) not in initial :
                                    initial.append(list(potentialNumber))
            return answer



if __name__=="__main__":
    k = 2
    n = 18
    print(Solution().combinationSum3(k=k,n=n))