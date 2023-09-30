import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    listOfSalaries=set(employee['salary'].values)
    if len(listOfSalaries)<2:
        salary=None
    else:
        salary=sorted(listOfSalaries,reverse=True)[1]
    
    return pd.DataFrame(data=[salary],columns=["SecondHighestSalary"])


if __name__=="__main__":
    employee=pd.DataFrame(data=[
                                (1,100),
                                # (2,200),
                                # (3,300)
                                ], 
                          columns=['id','salary'])
    print(second_highest_salary(employee=employee))