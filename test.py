from itertools import permutations
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n1=str(n)
        n2=permutations(n1)
        n3=sorted(set([int(''.join(ns)) for ns in n2]))
        index=n3.index(n)
        if index<len(n3)-1:
            return n3[index+1]
        else: return -1


if __name__=="__main__":    
    n=23
    print(Solution().nextGreaterElement(n=n))
