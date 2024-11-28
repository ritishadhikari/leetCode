from typing import List
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target.sort()
        itr,ist=0,0
        stack=[]
        result=[]
        for c in range(1,n+1):
            if itr==len(target):
                return result
            else:
                stack.append(c)
                result.append("Push")
                if target[itr]!=stack[ist]:
                    stack.pop()
                    result.append("Pop")
                else:
                    ist+=1
                    itr+=1
        return result


if __name__=="__main__":
    target = [1,2,3]
    n=3
    print(Solution().buildArray(target=target,n=n))