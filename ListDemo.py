print("Demostration of List")

# data : Heterogenous
# ordered : yes
# indexed : yes
# Mutable :yes
# Duplicates : yes

data = [11,21,51,101]
data1 = [10,90.80,True,"Hello"] #Heterogeneous

print("Data is Heterogenous :",data1)
print("Data is orderd :",data1)
print("Data at index : ",data1[2])
print("Data with Duplicate elements:",data)


print("List is mutable")
data.append(28)
print("Data after append :")
data.pop()
print("Data after pop : ".data)

