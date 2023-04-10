import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

def CreateXlsxFile(filename):
    Data = {"Weight":[35,47,90,48,90,35,92,35,35,35,96,43,110,35,95],
            "Pattern":["Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth"],
            "Label":["Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket","Tennis","Tennis","tennis","Cricket","Tennis","Cricket","Tennis","Cricket"]
        }

    df = pd.DataFrame(Data, columns = ["Weight","Pattern","Label"])

    writerInFile = pd.ExcelWriter(filename)

    df.to_excel(writerInFile,sheet_name="sheet1",index=False)

    writerInFile.save()

    return filename


def showGraph(file):
    df = pd.read_excel(file)

    x = df["Weight"]
    y = df["Pattern"]
    z= df["Label"]

    plt.scatter(x,y,linewidths=1, alpha=.7,edgecolor='k')
    plt.xlabel("Weight")
    plt.ylabel("Pattern")
    plt.show()



def getFile(file):
    df = pd.read_excel(file)
    print(df)

    # preprocessing to data
    le = preprocessing.LabelEncoder()
    Encoder_pattern=le.fit_transform(df["Pattern"])
    Encoder_label = le.fit_transform(df["Label"])

    Feature = list(zip(df["Weight"],Encoder_pattern))

    model = KNeighborsClassifier(n_neighbors=2)

    model.fit(Feature,Encoder_label)

    predicted = model.predict([[95,1]])


    if predicted==1:
        print("your object looks like a Tennis ball")
    else:
        print("your object looks like a cricket ball")

def main():

    file_name = CreateXlsxFile(filename="Ball.xlsx")

    showGraph(file_name)

    getFile(file_name)


if __name__ == "__main__":
    main()