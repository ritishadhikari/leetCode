from typing import List
from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners,losers={},{}
        for winner,loser in matches:
            if winner not in winners:
                winners[winner]=1
            else:
                winners[winner]+=1
            if loser not in losers:
                losers[loser]=1
            else:
                losers[loser]+=1
        
        winnerList,loserList=[],[]
        for winner,winningCount in winners.items():
            if winner not in losers:
                winnerList.append(winner)
        for loser,losingCount in losers.items():
            if losingCount==1:
                loserList.append(loser)
        
        return [sorted(winnerList),sorted(loserList)]
            
if __name__=="__main__":
    matches = [[2,3],[1,3],[5,4],[6,4]]
    print(Solution().findWinners(matches=matches))