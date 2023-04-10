# application is used to demostrates creation of series using pandas with different ways


import pandas as pd
import numpy as np

s= pd.Series()
print(s)

data= np.array(['a','b','c','d'])
s = pd.Series(data)

print(s[0])

data= np.array(['a','b','c','d'])
s= pd.Series(data,index=[100,101,102,103])
print(s[101])

data= {'a':1,"b":2,"c":3,"d":4}
s= pd.Series(data)
print(s)
print(s["a"])

s= pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s['a'])