from typing import List
from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        lookup = {}
        for b in bank:
            lookup[b] = False

        q = deque([(startGene, 0)])
        while q:
            cur, level = q.popleft()
            if cur == endGene:
                return level

            for i in range(len(cur)):
                for c in ['A', 'T', 'C', 'G']:
                    if cur[i] == c:
                        continue

                    next_str = cur[:i] + c + cur[i+1:]
                    if next_str in lookup and lookup[next_str] == False:
                        q.append((next_str, level+1))
                        lookup[next_str] = True


if __name__=="__main__":
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]
    print(Solution().minMutation(startGene=startGene,endGene=endGene,bank=bank))