import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    
    lowSalary,averageSalary,highSalary=0,0,0
    for salary in accounts['income'].values:
        if salary<20000:
            lowSalary+=1
        elif salary>=20000 and salary<=50000:
            averageSalary+=1
        else:
            highSalary+=1
    
    return pd.DataFrame(data=[('Low Salary',lowSalary),
                       ('Average Salary',averageSalary),
                       ('High Salary',highSalary)
                       ],
                       columns=['category','accounts_count'])



if __name__=="__main__":
    accounts=pd.DataFrame(data=[(3,108939),
                                (2,12747),
                                (8,87707),
                                (6,91796)],
                          columns=['account_id','income'])
    print(count_salary_categories(accounts=accounts))