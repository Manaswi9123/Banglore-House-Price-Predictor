# Banglore-House-Price-Predictor
# 🏠 Bengaluru House Price Predictor (End-to-End)

Predicting real estate prices in a dynamic market like Bengaluru requires handling high-cardinality categorical data and outliers. This repository features a full-stack Machine Learning solution that cleans raw data, trains a regularized regression model, and deploys it via a **Flask** web server.

---

## 🛠️ The Development Stack
* **IDE:** PyCharm (with isolated `venv` environment).
* **Data Science:** Python, Pandas, NumPy.
* **Machine Learning:** Scikit-Learn (`Ridge Regression`, `OneHotEncoder`, `Pipeline`).
* **Web Backend:** Flask.
* **Web Frontend:** HTML5, Bootstrap 5, JavaScript (AJAX).
* **Data Source:** Bengaluru_House_Data (Kaggle).

---

## 🧠 Project Workflow

### 1. Data Cleaning & Optimization (`BangloreHousePrice.ipynb`)
* **Preprocessing:** Handled missing values in `bath` and `size`, and converted inconsistent string values in `total_sqft` (like ranges "2100 - 2850") into numerical averages.
* **Feature Engineering:** Created a new `bhk` feature and filtered out extreme outliers (e.g., properties with an unrealistic price-per-square-foot or suspicious BHK-to-area ratios).
* **Dimensionality Management:** Reduced high-cardinality in the `location` column by labeling locations with fewer than 10 data points as "Other."
* **Modeling:** Compared Linear Regression, Lasso, and Ridge. **Ridge Regression** was selected for its superior ability to handle multicollinearity, achieving an $R^2$ score of approximately **0.86**.

### 2. Web Application & Deployment (`App.py`)
* **Environment:** Developed using a **PyCharm Virtual Environment (venv)** to ensure dependency isolation and reproducibility.
* **Flask Backend:** Created routes to serve the interactive UI and a dedicated `/predict` endpoint that processes JSON/Form data.
* **Frontend Design:** Built a responsive interface using **Bootstrap 5** with a "bisque" and "cadetblue" color scheme for a professional look.
* **Seamless UX:** Integrated **AJAX (XMLHttpRequest)** so that users receive price predictions instantly without the page refreshing.

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Manaswi9123/Python-DataScience-Fundamentals.git](https://github.com/Manaswi9123/Python-DataScience-Fundamentals.git)
