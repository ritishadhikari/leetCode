import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks['capital_gain_loss']=stocks.apply(lambda s: s['price']*-1 if s['operation']=="Buy" else s['price']*1, axis=1 )
    ans=stocks.groupby(by="stock_name")["capital_gain_loss"].sum()
    ans=ans.reset_index(drop=False)
    return ans
        


if __name__=="__main__":
    stockName=["Leetcode","Corona Masks","Leetcode","Handbags","Corona Masks",
               "Corona Masks","Corona Masks","Handbags","Corona Masks"]
    operation=["Buy","Buy","Sell","Buy","Sell","Buy","Sell","Buy","Sell","Sell"]
    operationDay=[1,2,5,17,3,4,5,6,29,10]
    price=[1000,10,9000,30000,1010,1000,500,1000,7000,10000]
    stocks=pd.DataFrame(data=zip(stockName,operation,operationDay,price),
                        columns=["stock_name","operation","operation_day","price"])
    # print(stocks.head(2))
    print(capital_gainloss(stocks=stocks))