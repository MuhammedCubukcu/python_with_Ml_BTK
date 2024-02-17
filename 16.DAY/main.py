import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.mixture import GaussianMixture

# Veri setini yükleme
dataset = pd.read_csv('musteriler.csv')
X = dataset.iloc[:, 3:].values

# K-means için
kmeans = KMeans(n_clusters=3, init='k-means++')
kmeans.fit(X)

# Hiyerarşik kümeleme için
agg_clustering = AgglomerativeClustering(n_clusters=3)
agg_clustering.fit(X)

# Gaussian Karışım Modelleri için
gmm = GaussianMixture(n_components=3)
gmm.fit(X)

# K-means'in inertia değerlerini hesaplama
kmeans_results = []
for i in range(1, 20):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    kmeans_results.append(kmeans.inertia_)

# Hiyerarşik kümeleme için inertia değerlerini hesaplama
agg_results = []
for i in range(1, 20):
    agg_clustering = AgglomerativeClustering(n_clusters=i)
    agg_clustering.fit(X)
    # Küme merkezlerini alma işlemi olmadığı için inertia değeri bulunmamaktadır.
    # Bu yüzden doğrudan modelin skorunu (silhouette_score gibi) alabiliriz.
    # Aşağıda örnek bir skor hesaplama kodu yoktur.

# Gaussian Karışım Modelleri için BIC değerlerini hesaplama
gmm_results = []
for i in range(1, 20):
    gmm = GaussianMixture(n_components=i)
    gmm.fit(X)
    gmm_results.append(gmm.bic(X))

# Sonuçları görselleştirme
plt.figure(figsize=(12, 6))

# K-means için
plt.subplot(1, 3, 1)
plt.plot(range(1, 20), kmeans_results, marker='o')
plt.title('K-means Inertia Değeri')
plt.xlabel('Küme Sayısı')
plt.ylabel('Inertia')

# Hiyerarşik kümeleme için
plt.subplot(1, 3, 2)
# Burada doğrudan bir skor hesaplanmadığı için örnek bir kod yoktur.

# Gaussian Karışım Modelleri için
plt.subplot(1, 3, 3)
plt.plot(range(1, 20), gmm_results, marker='o')
plt.title('GMM BIC Değeri')
plt.xlabel('Bileşen Sayısı')
plt.ylabel('BIC')

plt.tight_layout()
plt.show()