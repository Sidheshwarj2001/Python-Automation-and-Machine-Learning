import pandas as pd
print("Empty data frame")
df = pd.DataFrame()
print(df)

print("DataFrame with list")
data = [1,2,3,4,5]
df= pd.DataFrame(data)
print(df)

print("Dataframe with nested list")
data = [["PPA",4],["LB",3],["PYTHON",3],["ANGULAR",3]]
df = pd.DataFrame(data,columns=["Course","Duration"])
print(df)

print("DataFrame using nested list in the dictionary")
data = {"NAME":["PPA","LB","PYTHON","ANGULAR"],"DURATION":[3,3,4,3]}
df = pd.DataFrame(data)
print(df)

print("DataFrame using nested dict in the list")
data= [{"Name":"PPA","Duration":4,"FEE":18000},{"Name":"LB","Duration":3,"FEE":16000},{"Name":"Python","Duration":3.5,"FEE":16500},{"Name":"Angular","Duration":3,"FEE":17000}]
df = pd.DataFrame(data)
print(df)

print("DataFrame with dictionary")
d = {"One":pd.Series([1,2,3],index=["a","b","c"]),
     "Two":pd.Series([1,2,3,4],index=["x","y","z","w"])}

df = pd.DataFrame(d)
print(df["Two"])