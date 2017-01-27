from sklearn.cluster import KMeans
import numpy as np

def kmeans_clustering(current_matirx):
    kmeans = KMeans(n_clusters=10, random_state=0).fit(current_matirx)
    return kmeans.labels_