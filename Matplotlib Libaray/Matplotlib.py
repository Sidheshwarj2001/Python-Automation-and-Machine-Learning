import pandas as pd
import matplotlib.pyplot as plt


exce_file = "Marvellous.xlsx"
data = pd.read_excel(exce_file)

print("All data from excel file")
print(data)

print("First 5 rows from file is ")
print(data.head())

print('first 3 rows from file is')
print(data.head(3))

print("Last 5 rows from file is")
print(data.tail())

print("Last 3 rows from file is ")
print(data.tail(3))

sorted_data = data.sort_values(["Name"],ascending=True)
print("Sorted data is : ")
print(sorted_data)

data["Age"].plot(kind="hist")
plt.show()

data["Age"].plot(kind="barh")
plt.show()