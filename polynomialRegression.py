import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#--data---
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([3, 5, 8, 12, 18, 22, 28, 32, 38, 42])


poly    = PolynomialFeatures(degree=2)
X_poly  = poly.fit_transform(X)


model   = LinearRegression().fit(X_poly, y)
y_pred  = model.predict(poly.transform(X))

predicted = model.predict(X_poly)
plt.scatter(X, y, color='black', label='Data points')


   
plt.plot(X, y_pred, color='red', label='Predicted sales')

plt.xlabel('Years of Experience')
plt.ylabel('Salary (Lakhs)')
plt.title('Polynomial Regression — Degree Comparison')
plt.legend()

plt.show()