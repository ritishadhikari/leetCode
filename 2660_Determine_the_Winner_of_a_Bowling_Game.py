from typing import List

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        
        def get_player_score(playerHits):
            score=1
            for i,hit in enumerate(playerHits):
                if i==0:
                    score+=hit
                elif i==1:
                    if playerHits[0]==10:
                        score+=2*hit
                    else:
                        score+=hit
                else:
                    if playerHits[i-1]==10 or playerHits[i-2]==10:
                        score+=2*hit
                    else:
                        score+=hit
            return score
        
        score1=get_player_score(playerHits=player1)
        score2=get_player_score(playerHits=player2)

        if score1>score2: 
            return 1
        elif score2>score1:
            return 2
        else:
            return 0

if __name__=="__main__":
    player1=[2,3]
    player2=[4,1]
    print(Solution().isWinner(player1=player1,player2=player2))