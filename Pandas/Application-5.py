# is used to demonstrates operations on excel file using pandas library

import pandas as pd

excel_file = 'Marvellous (1).xlsx'

data = pd.read_excel(excel_file)

print(data.head())

data_sheet = pd.read_excel(excel_file,sheet_name=0,index_col = 0)
print(data_sheet)

xlsx = pd.ExcelFile(excel_file)
data_sheets = []

for sheet in xlsx.sheet_names:
       print(sheet)
       data_sheets.append(xlsx.parse(sheet))

data = pd.concat(data_sheets)
print(data)