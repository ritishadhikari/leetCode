import pandas as pd
from math import inf

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores=scores.sort_values(by='score',ascending=False)
    rankVal=0
    rankList=[]
    prevScore=inf
    for score in scores['score']:
        if score<prevScore:
            rankVal+=1
        rankList.append(rankVal)
        prevScore=score
    scores['rank']=rankList

    return scores[['score','rank']]



if __name__=="__main__":
    scores=pd.DataFrame(data=[[1,3.5],[2,3.65],[3,4.0],
                              [4,3.85],[5,4.0],[6,3.65]],
                              columns=['id','score'])
    print(order_scores(scores=scores))