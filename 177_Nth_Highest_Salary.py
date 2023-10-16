import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salaries=list(set(employee['salary'].values.tolist()))
    columnName=f"getNthHighestSalary({N})"
    if len(salaries)<N:
        return pd.DataFrame(data=[None],columns=[columnName])
    else:
        return pd.DataFrame(data=[sorted(salaries,reverse=True)[N-1]],columns=[columnName])

if  __name__=="__main__":
    employee=pd.DataFrame(data=[[1,300],
                                [2,300],
                                [3,300]],
                          columns=['id','salary']
                                )
    
    print(nth_highest_salary(employee=employee,N=2))