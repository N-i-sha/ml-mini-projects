
[README.md](https://github.com/user-attachments/files/26356154/README.md)
# 🤖 Machine Learning Mini Projects

A collection of beginner ML projects built with Python, Scikit-learn, NumPy, and Matplotlib.

---

## 📁 Project Structure

```
├── linear_regression.py        # House Price Prediction
├── polynomial_regression.py    # Sales Prediction
├── kmeans_clustering.py        # K-Means Clustering
└── README.md
```

---

## 📌 Projects Overview

### 1. 🏠 Linear Regression — House Price Prediction
Predicts house prices (in Lakhs) based on house size (sq ft).
- Trains a Linear Regression model on 10 samples
- Plots scatter data (blue) and regression line (red)

### 2. 📈 Polynomial Regression — Sales Prediction
Captures non-linear relationships using a Degree-2 Polynomial model.
- Uses `PolynomialFeatures(degree=2)` to transform features
- Plots actual data points (black) vs predicted curve (red)

### 3. 🔵 K-Means Clustering
Groups 9 two-dimensional data points into 3 clusters.
- Uses `KMeans(n_clusters=3)`
- Color-codes clusters and marks centers with a red star ★

---

## 🛠️ Tech Stack

- **NumPy** — Numerical operations
- **Matplotlib** — Data visualization
- **Scikit-learn** — ML models & preprocessing

---

## ⚙️ Installation & Setup

```bash
# Clone the repo
git clone https://github.com/your-username/ml-mini-projects.git
cd ml-mini-projects

# Install dependencies
pip install numpy matplotlib scikit-learn

# Run any script
python linear_regression.py
python polynomial_regression.py
python kmeans_clustering.py
```

---

## 🎯 Concepts Covered

- Supervised Learning (Linear & Polynomial Regression)
- Unsupervised Learning (K-Means Clustering)
- Feature Transformation with `PolynomialFeatures`
- Data Visualization with Matplotlib

---

## 👨‍💻 Author

**Your Name** — [@your-username](https://github.com/your-username)

---

## 📄 License

Open-source under the [MIT License](LICENSE).
