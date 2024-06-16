import pandas as pd
from math import inf
def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    tracker={}
    for rid,aid,_ in request_accepted.values:
        if aid not in tracker:
            tracker[aid]=[]
        tracker[aid].append(rid)
        
        if rid not in tracker:
            tracker[rid]=[]
        tracker[rid].append(aid)
    
    maxFriends=-inf
    friendMostFriends=None
    for friend,friends in tracker.items():
        if len(friends)>maxFriends:
            maxFriends=len(friends)
            friendMostFriends=friend
    return pd.DataFrame(
        data=[[friendMostFriends,maxFriends]],
        columns=["id","num"]
    )


if __name__=="__main__":
    request_accepted=pd.DataFrame(
        data=zip(
            [1,1,2,3],
            [2,3,3,4],
            ["2016-06-03","2016-06-08",
             "2016-06-08","2016-06-09"]
        ),
        columns=["requester_id","accepter_id","accept_date"]
    )
    print(most_friends(request_accepted=request_accepted))
    