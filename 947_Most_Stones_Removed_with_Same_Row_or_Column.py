from typing import List
from collections import defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        length=len(stones)
        # First Create rowDict and colDict which contains the 
        # index of the rows and the cols in stones array
        rowDict=defaultdict(lambda : set())
        colDict=defaultdict(lambda : set())

        for ind,stone in enumerate(iterable=stones):
            rowDict[stone[0]].add(ind)
            colDict[stone[1]].add(ind)

        # Update The rowDict and ColDict
        counts=0
        for i in range(length):
            r,c=stones[i]
            if r in rowDict and c in colDict:
                stack={i}
                count=-1
                while stack:
                    index=stack.pop()
                    count+=1
                    r,c=stones[index]
                    if r in rowDict:
                        stack.update(rowDict[r])
                        rowDict.pop(r)
                    if c in colDict:
                        stack.update(colDict[c])
                        colDict.pop(c)
                    if index in stack: stack.remove(index)
                counts+=count
        return counts

if __name__=="__main__":
    stones = [[0,1],[0,2],[4,3],[2,4],[0,3],[1,1]]

    print(Solution().removeStones(stones=stones))


    '''
    
    stones = [[0,1],[0,2],[4,3],[2,4],[0,3],[1,1]]
[
	0	1x	1x	1x	0
	0	1x	0	0	0
	0	0	0	0	1x
	0	0	0	0	0
	0	0	0	1x	0
]
done={0,1,4,5,2}
stack={0}
colDict={1: {0, 5}, 2: {1}, 3: {2, 4}, 4: {3}}
rowDict={0: {0, 1, 4}, 4: {2}, 2: {3}, 1: {5}}

stack={1,4,5}
colDict={2: {1}, 3: {2, 4}, 4: {3}}
rowDict={4: {2}, 2: {3}, 1: {5}}

stack={4,5}
colDict={3: {2, 4}, 4: {3}}
rowDict={4: {2}, 2: {3}, 1: {5}}

stack={}
colDict={4: {3}}
rowDict={2: {3}}

stack={3}
colDict={4: {3}}
rowDict={2: {3}}
    
    '''