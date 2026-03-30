import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample data
X = np.array([
    [1, 2], [1, 4], [2, 2],
    [5, 8], [6, 9], [5, 7],
    [9, 3], [8, 2], [9, 4]
])

# Train model
model = KMeans(n_clusters=3, random_state=42)
model.fit(X)

# Predictions
labels  = model.labels_
centers = model.cluster_centers_

# Plot
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=100)
plt.scatter(centers[:, 0], centers[:, 1], color='red', marker='*', s=200, label='Centers')
plt.title('K-Means Clustering')
plt.legend()
plt.show()