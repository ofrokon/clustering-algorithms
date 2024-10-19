import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, DBSCAN
from sklearn.datasets import make_blobs, make_moons
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.mixture import GaussianMixture

def save_plot(fig, filename):
    plt.show()
    fig.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close(fig)

def plot_kmeans():
    # Generate sample data
    X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=4, random_state=0)
    labels = kmeans.fit_predict(X)

    # Plot the results
    fig, ax = plt.subplots(figsize=(10, 8))
    scatter = ax.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
    ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
                marker='x', s=200, linewidths=3, color='r', label='Centroids')
    ax.set_title('K-Means Clustering')
    ax.legend()
    plt.colorbar(scatter)
    save_plot(fig, 'kmeans_clustering.png')

def plot_hierarchical():
    # Generate sample data
    np.random.seed(0)
    X = np.random.rand(50, 2)

    # Perform hierarchical clustering
    Z = linkage(X, method='ward')

    # Plot the dendrogram
    fig, ax = plt.subplots(figsize=(10, 7))
    dendrogram(Z, ax=ax)
    ax.set_title('Hierarchical Clustering Dendrogram')
    ax.set_xlabel('Sample Index')
    ax.set_ylabel('Distance')
    save_plot(fig, 'hierarchical_clustering.png')

def plot_dbscan():
    # Generate sample data
    X, _ = make_moons(n_samples=200, noise=0.05, random_state=0)

    # Perform DBSCAN clustering
    dbscan = DBSCAN(eps=0.3, min_samples=5)
    labels = dbscan.fit_predict(X)

    # Plot the results
    fig, ax = plt.subplots(figsize=(10, 8))
    scatter = ax.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
    ax.set_title('DBSCAN Clustering')
    plt.colorbar(scatter)
    save_plot(fig, 'dbscan_clustering.png')

def plot_gmm():
    # Generate sample data
    np.random.seed(0)
    X = np.concatenate([np.random.normal(0, 1, (100, 2)),
                        np.random.normal(3, 1.5, (100, 2))])

    # Perform GMM clustering
    gmm = GaussianMixture(n_components=2, random_state=0)
    labels = gmm.fit_predict(X)

    # Plot the results
    fig, ax = plt.subplots(figsize=(10, 8))
    scatter = ax.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
    ax.set_title('Gaussian Mixture Model Clustering')
    plt.colorbar(scatter)
    save_plot(fig, 'gmm_clustering.png')

if __name__ == "__main__":
    plot_kmeans()
    plot_hierarchical()
    plot_dbscan()
    plot_gmm()
    print("All visualizations have been saved as PNG files.")