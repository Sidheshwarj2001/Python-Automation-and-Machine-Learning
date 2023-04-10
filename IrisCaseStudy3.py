from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from scipy.spatial import distance

def euc(a,b):
    return distance.euclidean(a,b)

class MarvellousKNeighborsClassifier:

    def fit(self,trainingdata,trainingtarget):
        self.trainingData = trainingdata
        self.trainiTargetTarget = trainingtarget

    def closest(self,row):
        minimumdistance = euc(row,self.trainingData[0])
        minimumindex = 0

        for i in range(1,len(self.trainingData)):
            Distance = euc(row,self.trainingData[i])
            if Distance < minimumdistance:
                minimumdistance=Distance
                minimumindex = i

        return self.trainingData[minimumindex]


    def predict(self,TestData):
        prediction = []
        for value in TestData:
            result = self.closest(value)
            prediction.append(result)

        return prediction

def MarvellousML():
    Dataset = load_iris()       # 1 Load the data

    Data = Dataset.data
    Target = Dataset.target

    # step 2. manipulating the data
    Data_train, Data_test, Target_train, Target_test = train_test_split(Data, Target, test_size = 0.5)
    # print(Data_train)
    # print(Target_train)

    Classifier = MarvellousKNeighborsClassifier()

    # step3. Build the model
    Classifier.fit(Data_train, Target_train)

    # step 4 .test the model
    Predictions = Classifier.predict(Data_test)

    #
    Accuracy = accuracy_score(Target_test, Predictions)

    # step 5 . Improve - missing

    return Accuracy

def main():
    Ret = MarvellousML()

    print("Acuracy of Iris dataset with KNN is ",Ret * 100)

if __name__ == "__main__":
    main()