#cross reference employee list with active liscened users

#Core Python Module
from pathlib import Path 

#pip install pandas openpyxl
import pandas as pd 

#excel file path of former employees and if there's any errors it throws a error message
try:
    formerEmployees = pd.read_excel("C:\\script\\eFiles\\Employees2023.xlsx")
except Exception as e:
    print(f"Error reading input Excel file: {e}")


#excel file of licensed microsoft o365 users and if there's any errors it throws a error message
try: 
    licensedUsers = pd.read_excel("C:\\script\\eFiles\\users14_02_23.xlsx")
except Exception as e:
    print(f"Error reading input Excel file: {e}")


#merges the two files based on the two colums names if names match it will be merged
result = pd.merge(formerEmployees, licensedUsers, on=['FirstName', 'Surname'])

#present results in a new excel file
result.to_excel("formerEmployee_with_activeLicense.xlsx", index=False)


