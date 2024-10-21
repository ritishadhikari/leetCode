import pandas as pd
from collections import Counter
def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    answer=0
    for i,val in insurance.iterrows():
        tiv2015=val['tiv_2015']
        if len(insurance.loc[insurance['tiv_2015']==tiv2015])>1:  # First Condition is satisfied
        # if count[tiv2015]>1:  
            lat=val['lat']
            lon=val['lon']
            dfLatLong=insurance.loc[
                (insurance['pid']!=val['pid']) &
                (insurance['lat']==lat) &
                (insurance['lon']==lon)
                ]
            if len(dfLatLong)==0:  # Second Condition is Satisfied
                answer+=val['tiv_2016']

    return pd.DataFrame(data=[answer],columns=['tiv_2016'])  

if __name__=="__main__":
    insurance=pd.DataFrame(data=zip(
        [1,2,3,4],
        [10,20,10,10],
        [5,20,30,40],
        [10,20,20,40],
        [10,20,20,40]
    ),columns=["pid","tiv_2015","tiv_2016","lat","lon"])
    print(find_investments(insurance=insurance))