# In this application is create dataframe using pandas and write the content
# of that dataframe in xlsx file using ExcelWriter

import pandas as pd

data = {"NAME":["PPA","PYTHON","LB","ANGULAR"],
        "DURATION" : [4,3.5,4,3],
        "FEE" : [18000,16500,16000,17000]
        }

df = pd.DataFrame(data)
print(df)

writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
df.to_excel(writer,sheet_name= "Sheet1")

writer.save()
