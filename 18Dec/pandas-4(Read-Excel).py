import pandas as pd

excel_file = ""
df = pd.read_excel(excel_file)

print(df.head())

df_sheet = pd.read_excel(excel_file,sheet_name=0,index_col=0)
print(df_sheet.head())
