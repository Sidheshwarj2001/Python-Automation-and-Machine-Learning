import pandas as pd
import numpy as np

data = [1,2,3,4,5]
df = pd.DataFrame(data)
# print(df)

print("DataFrame with list")
data = [["PPA",4,18000],["LB",2,18200],["python",5,18100],["Angular",4,18300],["LPS",5,21000]]
df = pd.DataFrame(data,columns=['Name',"Duration","Fees"])
# print(df)

#DataFrame using Dictionary
data = {'Name':["PPA","LB","Python","LSP"],"Duration":[4,3,3,4],"Fees":[18500,18300,18200,21100]}
data = {'Name':["PPA","LB","Python","LSP"],"Duration":[4,3,3,4],"Fees":[18500,18300,18200,21100]}
df = pd.DataFrame(data)
# print(df)

data = [{"Name":"PPA","Duration":4,"Fees":18500},{"Name":"LB","Duration":3,"Fees":18200},{"Name":"Python","Duration":3,"Fees":18000},{"Name":"LSP","Fees":21500},]
df = pd.DataFrame(data)
print(df)