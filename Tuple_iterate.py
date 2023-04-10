# data : Heterogenous
# ordered : yes
# indexed : yes
# Mutable :no
# Duplicates : yes

print("Demostration of list")
Data = (11,21,51,101)


print("Output using for")

for no in Data:
    print(no,end=" ")

print("\n__________________________________________________")

print("Output using for with index : ")

for no in range(0,len(Data)):
    print(Data[no],end=" ")
print("\n_______________________________________________________")

print("Output using while witth index :")

i=0
while(i<len(Data)):
    print(Data[i],end=" ")
    i+=1

print("\n______________________________________________________________")
