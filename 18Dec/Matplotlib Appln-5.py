import pandas as pd
import matplotlib.pyplot as plt

excel_file = "Marvellous.xlsx"
df = pd.read_excel(excel_file)

print("All Data from excel file")
print(df)

print("First 5 rows from file")
print(df.head())

print("First 4 rows from file")
print(df.head(4))

print("Last 10 rows from file")
print(df.tail(10))

print("Last 5 rows from file")
print(df.tail())

print("shape of data",df.shape)

sorted_data = df.sort_values(['Name'],ascending=False)
print("Sorted DAta")
print(sorted_data)


print(df.head())

df_sheet = pd.read_excel(excel_file,sheet_name=0,index_col=0)
print(df_sheet.head())

df['Age'].plot(kind="hist")
plt.show()

df['Age'].plot(kind="barh")
plt.show()

