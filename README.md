# Customer Performance Analysis – Machine Learning Project

A full-stack Machine Learning project that uses customer data to predict customer spending and marketing offer acceptance. The application combines Python, Scikit-learn, FastAPI, and an HTML frontend to demonstrate how predictive analytics can support marketing decisions.

## Project Overview

Understanding customer purchasing behavior helps businesses improve marketing strategies and make informed decisions.

This project applies two Machine Learning techniques:

- **Linear Regression:** Predicts customer spending using selected customer features.
- **Logistic Regression:** Predicts customer acceptance of a marketing offer.

A web interface allows users to enter customer information and request predictions from the trained models.

## Project Objectives

- Analyze customer demographic and purchasing data.
- Prepare data for Machine Learning.
- Train regression and classification models.
- Evaluate model performance using appropriate metrics.
- Build a web interface for customer predictions.
- Demonstrate the use of predictive analytics in marketing.

## Technologies Used

- **Python** – Programming and data processing
- **Pandas and NumPy** – Data manipulation
- **Scikit-learn** – Machine Learning
- **FastAPI** – Backend API
- **HTML, CSS, and JavaScript** – Frontend interface
- **Jupyter Notebook** – Model training and analysis
- **Joblib** – Saving and loading trained models

## Repository Structure

```text
Customer-Performance-Analysis-ML/
├── customer_performance.csv
├── main.py
├── index.html
├── train.ipynb
├── requirements.txt
├── metrics.json
├── response_model.joblib
├── spending_model.joblib
├── .gitignore
└── README.md
```

The dataset, saved models, and metrics are currently included at the repository root. They can be organized into `data/` and `models/` folders later if the application code is updated to use those paths.

## Dataset

The project uses customer demographic, purchasing, and marketing-related information.

Example features include:

- Income
- Age
- Number of children
- Recency of the last purchase
- Web purchases
- Catalog purchases
- Store purchases
- Website visits per month
- Purchases made using deals

The dataset is included in the repository as `customer_performance.csv`.

**Data format:** The training notebook expects a tab-separated file if it uses `sep="\t"`. Ensure the actual dataset format matches the notebook's data-loading settings.

## Machine Learning Models

### 1. Linear Regression

Linear Regression estimates customer spending using selected customer and purchasing features.

**Evaluation metrics:**
- R-squared (R²)
- Mean Absolute Error (MAE), if calculated
- Mean Squared Error (MSE), if calculated

### 2. Logistic Regression

Logistic Regression predicts whether a customer accepts a marketing offer based on the target variable defined in the dataset.

**Evaluation metrics:**
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC, if calculated

The actual evaluation results should be taken from the project's saved metrics and training notebook.

## Installation and Setup

### Prerequisites

Install Python and ensure it is available in your terminal.

### Step 1: Clone the repository

```bash
git clone https://github.com/aiela-yamin6/Customer-Performance-Analysis-ML.git
cd Customer-Performance-Analysis-ML
```

### Step 2: Create a virtual environment

For Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```powershell
py -m pip install -r requirements.txt
```

## Training the Models

Open `train.ipynb` in VS Code or Jupyter Notebook.

1. Select the correct Python environment.
2. Run the notebook cells from top to bottom.
3. Review the data preparation and model training steps.
4. Check the evaluation results.
5. Confirm that the trained model files and metrics are saved to the locations expected by `main.py`.

## Running the Backend

Start the FastAPI application from the project directory:

```powershell
uvicorn main:app --reload
```

The API should be available at:

- API: http://127.0.0.1:8000
- Interactive API documentation: http://127.0.0.1:8000/docs

These addresses assume the FastAPI application is named `app` inside `main.py`.

## Opening the Frontend

With the backend running, open `index.html` in your web browser.

The frontend is configured to communicate with the local backend at `http://127.0.0.1:8000`. If necessary, check the API address configured in the JavaScript code.

## Example Customer Input

The following example illustrates the customer information used by the prediction interface:

```json
{
  "Income": 58138,
  "Age": 57,
  "Children": 0,
  "Recency": 58,
  "NumWebPurchases": 8,
  "NumCatalogPurchases": 10,
  "NumStorePurchases": 4,
  "NumWebVisitsMonth": 7,
  "NumDealsPurchases": 3
}
```

The accepted input fields depend on the features implemented in the trained models and backend API.

## Expected Outcomes

This project demonstrates how Machine Learning can be applied to customer analytics by estimating customer spending and predicting marketing offer acceptance.

The application provides a practical example of connecting trained predictive models to a web interface. Its usefulness depends on data quality, model performance, and appropriate interpretation of predictions.

## Limitations

- Predictions depend on the quality and representativeness of the dataset.
- Model performance may be affected by missing values and class imbalance.
- Predictions are estimates, not guarantees of future customer behavior.
- The local API configuration is intended for development and demonstration.

## Future Improvements

- Add more data visualizations and customer insights.
- Compare additional Machine Learning algorithms.
- Improve feature engineering and model evaluation.
- Add stronger input validation and error handling.
- Deploy the application online for easier access.

## Author

**Aiela Yamin**

Machine Learning Project – Customer Performance Analysis

GitHub: https://github.com/aiela-yamin6

## Purpose

This project was developed for educational purposes to demonstrate data analysis, Machine Learning, model evaluation, and full-stack application integration.
