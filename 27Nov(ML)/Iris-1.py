from sklearn.datasets import load_iris

iris = load_iris()
# print(iris)

print("Features names of the iris data set")
print(iris.feature_names)

print("target name of iris data set ")
print(iris.target_names)

print("first 10 elements from the iris data set")

for i in range(len(iris.target)):
    print("ID : %d , Label : %s, Feature : %s"%(i,iris.data[i],iris.target[i]))

