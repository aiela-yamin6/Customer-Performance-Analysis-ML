"""Small FastAPI service that serves predictions and saved model metrics."""

import json
from pathlib import Path

import joblib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parent
MODEL_DIR = ROOT / "models"

# Load both trained models when the API module starts.
spending_model = joblib.load(MODEL_DIR / "spending_model.joblib")
response_model = joblib.load(MODEL_DIR / "response_model.joblib")

app = FastAPI(title="Customer Campaign Prediction API")

# Permit a separately opened local HTML file to call this API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class CustomerFeatures(BaseModel):
    """The nine numeric values required by both models."""

    Income: float = Field(ge=0, example=58138)
    Age: float = Field(ge=0, example=57)
    Children: float = Field(ge=0, example=0)
    Recency: float = Field(ge=0, le=99, example=58)
    NumWebPurchases: float = Field(ge=0, example=8)
    NumCatalogPurchases: float = Field(ge=0, example=10)
    NumStorePurchases: float = Field(ge=0, example=4)
    NumWebVisitsMonth: float = Field(ge=0, example=7)
    NumDealsPurchases: float = Field(ge=0, example=3)


@app.post("/predict/regression")
def predict_spending(customer: CustomerFeatures):
    """Return predicted total spending in the dataset's currency units."""
    values = customer.model_dump()  # Pydantic validates and converts the JSON fields.
    prediction = spending_model.predict([list(values.values())])[0]
    return {"predicted_total_spend": float(prediction)}


@app.post("/predict/classification")
def predict_response(customer: CustomerFeatures):
    """Return an offer acceptance class and its estimated probability."""
    values = customer.model_dump()
    row = [list(values.values())]
    prediction = int(response_model.predict(row)[0])
    probability = float(response_model.predict_proba(row)[0][1])
    label = "Will accept" if prediction == 1 else "Will not accept"
    return {"prediction": prediction, "label": label, "probability": probability}


@app.get("/metrics")
def get_metrics():
    """Give the frontend the saved scores and chart data."""
    with (MODEL_DIR / "metrics.json").open(encoding="utf-8") as file:
        return json.load(file)
