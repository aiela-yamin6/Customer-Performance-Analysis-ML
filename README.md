# Customer Campaign Prediction App

A beginner-friendly full-stack machine learning example. It trains one model to estimate customer spending and a second model to estimate whether a customer accepts the latest offer. FastAPI serves predictions, and `index.html` displays the forms and evaluation charts.

## Dataset

Place the Customer Personality Analysis file at `data/customer_performance.csv`. It is **tab-separated**, so `train.ipynb` reads it with `sep="\t"`. The supplied project copy is already in that location.

## Setup

Open PowerShell in this project folder, then run:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

## Train the models

```powershell
py train.py
```

The script cleans the data, trains a linear regression and a balanced logistic regression, and writes both models plus `models/metrics.json`. It uses the notebook's separate 80/20 splits: a regular random split for regression and a stratified split for classification. It prints R-squared, accuracy, precision, recall, F1, and ROC-AUC when training finishes. You can also open `train.ipynb` in Jupyter or VS Code and run its six cells from top to bottom; it contains the same beginner-friendly steps.

## Run the backend

```powershell
uvicorn main:app --reload
```

The API is at `http://127.0.0.1:8000`; interactive API documentation is at `http://127.0.0.1:8000/docs`.

## Open the frontend

With the backend running, open `index.html` in a browser. The page calls the API at `http://127.0.0.1:8000`. If your backend uses another address, update `API_URL` near the top of the page's JavaScript.

## Example inputs

Both forms start with this sample customer: income `58138`, age `57`, children `0`, recency `58`, web purchases `8`, catalog purchases `10`, store purchases `4`, web visits this month `7`, and deal purchases `3`. You can also send the same fields to either prediction route, for example:

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
