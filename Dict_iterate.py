programming = {
    "c" : "Richie",
    "c++" :"stroustrup",
    "Java" : "gosling",
    "Python" : "Rossum",
    "c" : "thomson"
}
print(programming)
Batches = {
    "PPA" : 18000,
    "LB" : 16700,
    "Python" : 16500,
    "Angular" : 15000
}
print("\n____________________________________________________________\n")

print("Data of Dictionary is : ",Batches)

print("Data traversal using for loop")

for x in Batches:
    print("keys is : ",x)

print("\n____________________________________________________________\n")

for x in Batches:
    print("key  is : ",x," ::: values is : ",Batches[x])

print("\n____________________________________________________________\n")

for x in Batches:
    print(x," : ",Batches.get(x))

print("\n____________________________________________________________\n")

keyBatches = Batches.keys()
print(keyBatches)
print(type(keyBatches))


valueBatches = Batches.values()
print(valueBatches)
print(type(valueBatches))

