import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# ── Data ──────
# House size (sq ft) vs Price (in lakhs)
X = np.array([500, 700, 800, 1000, 1200, 1500, 1800, 2000, 2200, 2500]).reshape(-1, 1)
y = np.array([25,  35,  40,  52,   58,   72,   85,   92,   100,  115])

#Train Model 
model = LinearRegression().fit(X, y)


# Predictions 
y_pred = model.predict(X)


plt.subplot(1, 2, 1)
plt.scatter(X, y, color='blue',  label='Train data', zorder=3)

plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression line')
plt.xlabel('House Size (sq ft)')
plt.ylabel('Price (Lakhs)')
plt.title('Linear Regression')
plt.legend()
plt.show()