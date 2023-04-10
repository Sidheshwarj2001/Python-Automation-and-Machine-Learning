import numpy as np
import pandas as pd
from copy import deepcopy
from matplotlib import pyplot as plt

def KMean():
    print("__"*20)
    # set three centers the model should predict similar results
    center_1 = np.array([1,1])
    print(center_1)
    print("__"*20)

    center_2 = np.array([5,5])
    print(center_2)
    print("__"*20)

    center_3 = np.array([8,1])
    print(center_3)
    print("__"*20)

    # generate random data and center it to the three centers
    data_1 = np.random.randn(7,2)+center_1
    print("Element of first cluster with size "+str(len(data_1)))
    print(data_1)

    print("__"*20)

    data_2 = np.random.randn(7,2)+center_2
    print("Element of second cluseter with size "+str(len(data_2)))
    print(data_2)
    print("__"*20)

    data_3 = np.random.randn(7,2) + center_3
    print("Element of third cluseter with size "  + str(len(data_3)))
    print(data_3)
    print("__" * 20)

    data = np.concatenate((data_1,data_2,data_3),axis=0)
    print("Size of complete data set "+str(len(data)))
    print(data)
    print("__" * 20)

    plt.scatter(data[:,0],data[:,1],s=7)
    plt.title("Random dataset")
    plt.show()
    print("__" * 20)

    # numbers of clusters
    k = 3
#     number of training data
    n = data.shape[0]
    print("Total numbers of elements are ",n)
    print("__" * 20)

#     number of features in the data
    c = data.shape[1]
    print("Total number of Feature are",c)
    print("__" * 20)

#     generate random centers here we use sigma and mean to ensure it represent the whole data

    mean = np.mean(data,axis=0)
    print("Value of mean",mean)
    print("__" * 20)

# calculating standard deviation
    std = np.std(data,axis=0)
    print("Value of std",std)
    print("__" * 20)

    centers = np.random.randn(k,c)*std+mean
    print("Random points are",centers)

    print("__" * 20)

#     plot the data and the centers generated as random
    plt.scatter(data[:,0],data[:,1],c='r',s=7)
    plt.scatter(data[:,0],centers[:,1],marker = "*",c= 'g',s=150)
    plt.title("Input Dataset with random centroid")
    plt.show()
    print("__" * 20)

    center_old = np.zeros(centers.shape) #to store old centers
    centers_new = deepcopy(centers)  # store new centers

    print("Value of old centroids")
    print(center_old)

    print("__" * 20)

    print("Values of new centroids")
    print(centers_new)

    print("__" * 20)

    data.shape
    clusters = np.zeros(n)
    distance = np.zeros((n.k))

    print("initial distance are")
    print(distance)
    print("__" * 20)

    error = np.linalg.norm(centers_new-center_old)
    prinnt("Value fo errror is ",error)
    # when after an updata the estimate of thea center stay the same ,exit loop

    while error != 0:
        print("VAlue of error is ",error)
        # measure the distance to every center
        print("Measure the distance to every center")
        for i in range(k):
            print("Iteration number",i)
            distance[:,i]=np.linalg.norm(data-centers[i],axis=1)

            # Assign all training data to closet center
            clusters = np.argmin(distance,axis=1)

            center_old = deepcopy(centers_new)

            # calculate mean for every cluster and updata the center

            for i in range(k):
                centers_new[i] = np.mean(data[clusters==i],axis=0)
            error = np.linalg.norm(centers_new-center_old)

         # end of while
        centers_new

#     plot the daa and the centers generated as random
    plt.scatter(data[:,0],data[:,1],s=7)
    plt.scatter(centers_new[:,0],centers_new[:,1],marker="*",c='g',s=150)
    plt.show()

def main():
    print("Unsupersed Machine learning")
    print("Clustering using k mean algorithm")
    KMean()

if __name__ == "__main__":
    main()