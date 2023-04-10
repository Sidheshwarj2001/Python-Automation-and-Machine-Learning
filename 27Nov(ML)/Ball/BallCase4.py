from sklearn import tree

def BallPredictor(weight,surface):
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(Features, Labels)

    ret = obj.predict([[weight,surface]])

    if ret ==1:
        print("your object looks like a Tennis ball")
    else:
        print("your object looks like a cricket ball")

def main():
    print("____________________Ball Predictor case study____________________")
    print("Please enter the weight of your object in gram")
    weight = int(input())

    print("Please enter type of surface of you object (Rough / Smooth")
    surface = input()

    if surface.lower=="rough":
        surface = 1
    elif :
        surface = 0
    else:
        print("Invalid type of surface")
        exit()

    BallPredictor(weight,surface)

if __name__ == "__main__":
    main()