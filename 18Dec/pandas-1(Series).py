import pandas as pd
import numpy as np

data = np.array(['a','b','c','d'])
s = pd.Series(data)
# print(s[0])

# customize indexing
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[101,102,103,104])
# print(s[101])

data = {'a':0.1,'b':1.1,'c':2.1}
s = pd.Series(data)
# print(s)
# print(s['a']) #alphanumeric indexing

s = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'],dtype="int32")
print(s)