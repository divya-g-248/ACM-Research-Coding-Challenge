from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import csv


def calculate_WSS(points, kmax):
    sse = []
    for k in range(1, kmax+1):
        kmeans = KMeans(n_clusters = k).fit(points)
        centroids = kmeans.cluster_centers_
        pred_clusters = kmeans.predict(points)
        curr_sse = 0

    # calculate square of Euclidean distance of each point from its cluster center and add to current WSS
        for i in range(len(points)):
            curr_center = centroids[pred_clusters[i]]
            curr_sse += (points[i, 0] - curr_center[0]) ** 2 + (points[i, 1] - curr_center[1]) ** 2

        sse.append(curr_sse)
    return sse

# opening file and making a matrix from it
file = open("c:/Users/dearr/Documents/ACMCodingChallenge/Coding-Challenge/ClusterPlot.csv", "r")
csvReader = csv.reader(file, delimiter=',')
data = np.genfromtxt(file, delimiter= ',')

# delete first row and first column
data = np.delete(data, [0], 1)
data = np.delete(data, [0], 0)

# calling the method to calsulate WSS Scores
numClusters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
wssScores = []
wssScores = calculate_WSS(data, 10)

# creating graph
plt.plot(numClusters, wssScores)
plt.xlabel("Number of Clusters")
plt.ylabel("WSS Scores")
plt.title("Elbow Method Graph")
plt.show()
plt.savefig("c:/Users/dearr/Documents/ACMCodingChallenge/Coding-Challenge/elbowMethodGraph.png")
