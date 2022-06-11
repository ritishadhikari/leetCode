from typing import List
from collections import deque

class Solution:
    def letterCasePermutation(self,s:str) -> List[str]:
        count=0
        stack=deque()
        while count<len(s):
            size=max(len(stack), 1)
            while size>0:
                val=stack.popleft() if stack else ""              
                val2Append=s[count]
                if ord(val2Append)>=48 and ord(val2Append)<=57:
                    stack.append(val+val2Append)
                else:
                    stack.append(val+val2Append.lower())
                    stack.append(val+val2Append.upper())
                size-=1
            count+=1

        return stack




if __name__=="__main__":
    print(Solution().letterCasePermutation(s="a1b2"))