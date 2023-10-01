import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    filteredEmployee=employee[employee['id']!=employee['managerId']]
    managerIDs=filteredEmployee.groupby('managerId')['name'].count()
    managerIDs=managerIDs[managerIDs>=5].index.values
    managerNames=[]
    for manager in managerIDs:
        probablename=employee.loc[employee['id']==manager,"name"].values
        if probablename:
            name=probablename[0]
            managerNames.append(name)
    return pd.DataFrame(data=managerNames,columns=['name'])

if __name__=="__main__":
    data = [[101, 'John', 'A', None], 
            [102, 'Dan', 'A', 101], 
            [103, 'James', 'A', 101], 
            [104, 'Amy', 'A', 101], 
            [105, 'Anne', 'A', 101], 
            [106, 'Ron', 'B', 101]]
    employee = pd.DataFrame(data, 
                            columns=['id', 'name', 'department', 'managerId'])\
                                .astype({'id':'Int64', 'name':'object', 
                                         'department':'object', 'managerId':'Int64'})
    
    print(find_managers(employee=employee))