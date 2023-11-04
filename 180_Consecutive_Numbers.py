import pandas as pd
def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    secondLast=None
    last=None
    ans=[]
    for _,(id,num) in enumerate(logs.values):
        if num==last and last==secondLast:
            ans.append(num)
        secondLast,last=last,num
    
    return pd.DataFrame(data=[[j] for j in ans],columns=["ConsecutiveNums"])

if __name__=="__main__":
    logs=pd.DataFrame(data=[[1,1],[2,1],[3,1],
                            [4,2],[5,1],[6,2],[7,2]],
                            columns=["id","num"])
    print(consecutive_numbers(logs=logs))