print("Demostration of set : ")

# data : Heterogenous
# ordered : no
# indexed : no
# Mutable :yes
# Duplicates : no

Data = {11,21,51,101,21,11} #duplicate
data1 = {11,90.820,True,"hello"}

print("Fist set data : " ,Data)
print("Length of data: ",len(Data))
print("Data is hestrogenous :",data1)
print("Data is orderd :",data1)
# print("Data at index : ",data1[2]) #/not accessable
print("Data with Uninque elements:",Data)

print("set is mutable")
# Data.append(28)
# print("Data after append :")
# Data.pop()
# print("Data after pop : ",Data)

# insert element in set
Data.add(211)
print("Data after insertion : ",Data)

# remove element
Data.remove(211)
print("Data after remove : ",Data)

Data.discard(201)
print("Data after remove : ",Data)