from typing import List
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        lookUp={i:False for i in bank}
        q=[(startGene,0)]
        while q:
            seq,level=q.pop(0)
            if seq==endGene:    return level
            else:
                for i,ch in enumerate(seq):
                    for letter in ['A','C','G','T']:
                        if ch!=letter:
                            newSeq=seq[:i]+letter+seq[i+1:]
                            if newSeq in lookUp and lookUp[newSeq]==False:
                                q.append([newSeq,level+1])
                                lookUp[newSeq]=True
        return -1

if __name__=="__main__":
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]
    print(Solution().minMutation(startGene=startGene,endGene=endGene,bank=bank))