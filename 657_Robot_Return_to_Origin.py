class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pointer=[0,0]

        for move in moves:
            if move=="L":
                pointer[0]-=1
            elif move=="R":
                pointer[0]+=1
            elif move=="U":
                pointer[1]+=1
            else:
                pointer[1]-=1
        
        return True if pointer[0]==0 and pointer[1]==0 else False


if __name__=="__main__":
    moves="RRDD"
    print(Solution().judgeCircle(moves=moves))