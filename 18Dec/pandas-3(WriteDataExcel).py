import pandas as pd
import numpy as np

data = [1,2,3,4,5]
df = pd.DataFrame(data,columns=["Data"])

writer = pd.ExcelWriter("SidPandas.xlsx")

df.to_excel(writer,sheet_name="sheet1")

writer.save()
