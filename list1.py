
values = [1,2,3,4,5,6]

print(values)

print(type(values))


print(len(values))

# sizepf is byte
#  len give the length of element

values.insert(1,25)
print("Data after insert ",values)


values.insert(15,100) # it insert the values at the end of list because range is not 15
print("Data after insert is : ",values)
print("the size of list is now : ",len(values))


print(values[0])
print(values[1])
print(values[2])
print(values[3])

values.append(7) # add values at the last of list

print(values)

values.remove(4)
print(values)

values.append(7)
print(values)

print(type(values[2]))

values.append(90.89)
print(values)

