import pandas as pd
import re
import numpy as np

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users.loc[users['mail'].str.match(
        pat=r"[a-zA-Z]+[\w.-]*@leetcode\.com$"
    ),:]
    

if __name__=="__main__":
    users=pd.DataFrame(
        data=[
            [1,"Winston","winston@leetcode.comavd"],
            [2,"Jonathan","jonathanisgreat"],
            [3,"Annabelle","bella-@leetcode.com"],
            [4,"Sally","sally.come@leetcode.com"],
            [5,"Marwan","quarz#2020@leetcode.com"],
            [6,"David","david69@gmail.com"],
            [7,"Shapiro",".shapo@leetcode.com"]
              ],
              columns=['user_id',"name","mail"]
    )
    print(valid_emails(users=users))