# Import required library
from sklearn import tree

# Load the dataset
Features = [[35,"Rough"],[47,"Rough"],[90,"Smooth"],[48,"Rough"],[90,"Smooth"],[35,"Rough"],[92,"Smooth"],[35,"Rough"],[35,"Rough"],[35,"Rough"],[96,"Smooth"],[43,"Rough"],[110,"Smooth"],[35,"Rough"],[95,"Smooth"]]
Labels = ["Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket","Tennis","Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket"]

# Decide the Machine Learning Algorithm
obj = tree.DecisionTreeClassifier()

# Perform the training of model
obj = obj.fit(Features, Labels)

# Perform the testing
print(obj.predict([[97,"Smooth"]]))