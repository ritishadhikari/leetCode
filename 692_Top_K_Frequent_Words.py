from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        countDict=defaultdict(lambda: 0)
        itemCount=defaultdict(lambda: [])
        finalList=[]

        for char in words:
            if char not in countDict.keys():
                newCount=countDict[char]+1
                countDict[char]=newCount
                itemCount[newCount].append(char)
            else:
                itemCount[countDict[char]].remove(char)
                newCount=countDict[char]+1
                countDict[char]=newCount
                itemCount[newCount].append(char)

        while k:
            maxVal=max(itemCount.keys())
            maxList=sorted(itemCount.pop(maxVal))
            if len(maxList)<k:
                k=k-len(maxList)
                finalList+=maxList
            else:
                finalList+=maxList[:k]
                k=0

        return finalList


if __name__=="__main__":
    words = ["i","love","leetcode","i","love","coding"]
    k=2
    print(Solution().topKFrequent(words=words,k=k))