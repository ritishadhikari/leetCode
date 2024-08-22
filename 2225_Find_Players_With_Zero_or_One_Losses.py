from typing import List
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners,losers=set(),{}
        for winner,loser in matches:
            if winner not in winners:
                winners.add(winner)

            if loser in losers:
                losers[loser]=False  # Losers count is greater than 1
            else:
                losers[loser]=True  # Losers count is 1 
        
        winnerList,loserList=[],[]
        for winner in winners:
            if winner not in losers:
                winnerList.append(winner)
        for loser,status in losers.items():
            if status:
                loserList.append(loser)
        
        return [sorted(winnerList),sorted(loserList)]
            
if __name__=="__main__":
    matches = [[2,3],[1,3],[5,4],[6,4]]
    print(Solution().findWinners(matches=matches))