import numpy as np
import matplotlib.pyplot as plt
import random

def create_cluster(X, centroid_pts):
    cluster = {}
  # read about lambdas and np.linalg.form
  # https://stackoverflow.com/questions/32141856/is-norm-equivalent-to-euclidean-distance ,
  # here we are using order 1 to calculate normalized distance
    for x in X:
        value = min([(i[0],np.linalg.norm(x - centroid_pts[i[0]]))for i in enumerate(centroid_pts)], key=lambda s:s[1])[0]
        try:
            cluster[value].append(x)
        except:
            cluster[value] = [x]
    return cluster


def calculate_new_center(cluster):
    keys =sorted(cluster.keys())
    newmu = np.array([(np.mean(cluster[k],axis = 0))for k in keys])
    return newmu

def matched(new_centroids, old_centroids):
    return (set([tuple(a)for a in new_centroids]) == set([tuple(a)for a in old_centroids]))

def Apply_Kmeans(X, K, N):
    # Old centroids are generated for the first time
    old_centroids = np.random.randint(N, size = K)
    old_centroid_pts = np.array([X[i]for i in old_centroids])

    print("old  points:",old_centroids)
    print(old_centroid_pts)

    cluster_info = create_cluster(X, old_centroid_pts)

    print("Initial cluster information:")
    print(cluster_info)
    #these are the new centroids generated for the 1st time
    new_centroids = np.random.randint(N, size=K)
    new_centroid_pts = np.array([X[i] for i in new_centroids])

    print("new :", new_centroids)
    print(new_centroid_pts)
    itr = 0
    print("Graph after selecting initial clusters with initial centroids:")
    plot_cluster(old_centroid_pts,cluster_info,itr)

    # It will exit when old centroids points and new centroid points doesn't match
    while not matched(new_centroid_pts, old_centroid_pts):
        itr = itr + 1
        # for second iteration old centroid points equal to new centroid points
        old_centroid_pts = new_centroid_pts
        cluster_info = create_cluster(X,new_centroid_pts)
        plot_cluster(new_centroid_pts, cluster_info,itr)
        # New centroid points generated based on the mean of the points in the cluster
        new_centroid_pts = calculate_new_center(cluster_info)

    print("Results after final iteration:")
    #this is the final iteration
    plot_cluster(new_centroid_pts, cluster_info, itr)
    return


#used to plot the cluster
def plot_cluster(mu,cluster, itr):
    color = 10 * ['r.','g.','k.','c.','b.','m.']
    print('Iteration number : ',itr)
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=10)
    plt.scatter(mu[:,0],mu[:,1],marker = 'x', s = 150, linewidths = 5, zorder = 10)
    plt.show()


# It was the initial graph generated where the points generated in random from the arrays
def init_graph(N, p1, p2):
    X = np.array([(random.choice(p1),random.choice(p2))for i in range(N)])
    return X


def Simulate_Clusters():
    print(".........Starting Cluster Simulation.........")
    K = int(input("Enter the number of Sizes:"))
    firstArray = np.array([20, 30, 10, 25, 38, 48, 18, 29, 32, 59, 42, 22, 21, 34, 58, 47, 55, 39, 52, 57, 51, 31])
    secondArray = np.array([10, 12, 14, 20, 16, 18])
    X = init_graph(len(firstArray), secondArray, firstArray)
    plt.scatter(X[:, 0], X[:, 1])
    print(X)
    plt.show()
    Apply_Kmeans(X, K, len(X))

if __name__ == '__main__':
    Simulate_Clusters()