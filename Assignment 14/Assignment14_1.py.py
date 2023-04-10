from sklearn import tree
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

# step1 : load data
def playpredictor(filename):
    data = pd.read_csv(filename,index_col=0)

    print("Size of dataset : ",len(data))

    # step 2 :clean prepare and manipulate data

    feature_name = ["Whether","Temperature"]

    whether = data.Whether
    temperature = data.Temperature
    play = data.Play
    # print(whether)
    # print(temperature)
    # print(play)
    print("Name of Features",feature_name)

    #creating labelEncoder
    le = preprocessing.LabelEncoder()

    # converting string lable into number
    whether_encoded = le.fit_transform(whether)
    print(whether_encoded)

    temp_encoded = le.fit_transform(temperature)
    print(temp_encoded)

    label = le.fit_transform(play)

    # combining weather and temp into single list of tuple
    features = list(zip(whether_encoded,temp_encoded))

    # step 3 : train data
    model  = KNeighborsClassifier(n_neighbors = 3)

    # train the model using training sets

    model.fit(features,label)

    # step 4 :test model
    predicted = model.predict([[0,2]]) #0 overcast 2 mild
    print(predicted)

    return predicted

def main():
    print("_______marvellous infosystem_________")
    print("Machine learning algorithm")
    print("Play predictor application using k nearest knighbor algorithm")

    dataset = r"C:\Users\91774\Desktop\Marvellous_Infosystem_Code\Assignment\Assignment 14\PlayPredictor.csv"

    result = playpredictor(dataset)

    if result:
        print("Yes")
    else:
        print("NO")

if __name__ == "__main__":
    main()



