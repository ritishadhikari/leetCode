import pandas as pd
from collections import defaultdict

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    highest={}
    deptDict={id:dept for id,dept in department.values}
    tracker={}
    for empid,name,salary,depId in employee.values:
        if depId not in tracker:
            highest[depId]=[[name,salary]]
            tracker[depId]=salary
        else:
            if tracker[depId]<salary:
                highest[depId]=[[name,salary]]
                tracker[depId]=salary
            elif tracker[depId]==salary:
                highest[depId]=highest[depId]+[[name,salary]]

    # return highest
    highest=[(id,name,salary) for id,values in highest.items() for name,salary in values]
      

    ans=[]
    for depID,name,salary in highest:
        dept=deptDict[depID]
        ans.append([dept,name,salary])
    
    return pd.DataFrame(data=ans,columns=[
                                    "Department",
                                    "Employee",
                                    "Salary"
                                    ]
                                          )


if __name__=="__main__":
    employee=pd.DataFrame(data=[
        [1,"Joe",70000,1],
        [2,"Jim",90000,1],
        [3,"Henry",80000,2],
        [4,"Sam",60000,2],
        [5,"Max",90000,1]
        ],
        columns=['id','name','salary','departmentId']
        )
    department=pd.DataFrame(data=[
        [1,'IT'],
        [2,'Sales']
        ],
        columns=['id','name']
        )
    print(department_highest_salary(employee=employee,department=department))