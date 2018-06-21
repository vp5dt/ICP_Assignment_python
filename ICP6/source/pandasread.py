# import useful libraries
import pandas
import pylab as pl
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# using pandas read the csv file into variables
variables = pandas.read_csv('sample_stocks.csv')


# Y variable defined as returns and X variable defined as dividendyid
Y = variables[['returns']]
X = variables[['dividendyield']]

# PLot the elbow curve to find no of clusters best suits
# Nc is the range for the number of the clusters
Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i) for i in Nc]
kmeans
# percentage of variance explained by  no of clusters
score = [kmeans[i].fit(Y).score(Y) for i in range(len(kmeans))]
score
pl.plot(Nc,score)
pl.xlabel('Number of Clusters')
pl.ylabel('Score')
pl.title('Elbow Curve')
pl.show()
# End of elbow curve

pca = PCA(n_components=1).fit(Y)

pca_d = pca.transform(Y)

pca_c = pca.transform(X)

kmeans=KMeans(n_clusters=3)

kmeansoutput=kmeans.fit(Y)

kmeansoutput

pl.figure('3 Cluster K-Means')

pl.scatter(pca_c[:, 0], pca_d[:, 0], c=kmeansoutput.labels_)

pl.xlabel('Dividend Yield')

pl.ylabel('Returns')

pl.title('3 Cluster K-Means')

pl.show()
