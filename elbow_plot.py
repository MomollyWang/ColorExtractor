import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans,vq

def elbow(df):
    # use elbow plot to find the proper number for centroids/clusters
    distortions = []
    num_clusters = range(1, 10)

    for i in num_clusters:
        cluster_centers, distortion = kmeans(df[['scaled_red','scaled_blue','scaled_green']],i)
        distortions.append(distortion)
        
    # show elbow plot
    plt.plot(num_clusters, distortions)
    plt.xticks(num_clusters)
    plt.title('Elbow Plot for Color Extraction', size=18)
    plt.xlabel('Number of Clusters')
    plt.ylabel("Distortions")
    plt.show()