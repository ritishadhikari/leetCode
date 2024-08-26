from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ns=sorted([str(i+1) for i in range(n)])
        return [int(number) for number in ns]
        return ns


if __name__=="__main__":
    n=2
    print(Solution().lexicalOrder(n=n))