# 🚗 Car Price Prediction API

A FastAPI-based backend application that predicts the price of a vehicle using machine learning models trained on vehicle specifications and engine metadata.

### 🔗 Deployed API:

📍 [https://car-price-prediction-6wi1.onrender.com](https://car-price-prediction-6wi1.onrender.com)

---

## 📦 Features

* Clean and preprocessed vehicle metadata (make, model, year, fuel, engine, etc.)
* Feature engineering using pipelines
* Multiple model training and best model selection
* FastAPI for serving predictions
* Deployed using **Render**
* Tested using **Postman**

---

## 🔧 Tech Stack

* **Backend**: FastAPI
* **ML Models**: Scikit-learn
* **Deployment**: Render
* **Testing**: Postman

---

## 🚀 Getting Started

### ✅ Prerequisites

Make sure you have:

* Python 3.8+
* `pip` installed
* Optional: virtual environment (`venv` or `conda`)

---

### 🛠️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/Abhishek-R-Gupta/CAR-PRICE-PREDICTION.git
cd CAR-PRICE-PREDICTION/web/backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI app
uvicorn app.main:app --reload
```

---

## 🌐 API Reference

### ✅ `POST /predict`

Predicts the price of a car based on the given specifications.

#### 📄 Request Body (JSON)

| Parameter    | Type   | Description                                          |
| ------------ | ------ | ---------------------------------------------------- |
| `make`       | string | Manufacturer name (e.g., "Mercedes-Benz")            |
| `model`      | string | Model name (e.g., "Sprinter 2500")                   |
| `year`       | int    | Year of manufacture (e.g., 2023)                     |
| `engine`     | string | Engine type/spec (e.g., "16V DDI DOHC Turbo Diesel") |
| `cylinders`  | int    | Number of cylinders (e.g., 4)                        |
| `fuel`       | string | Fuel type (e.g., "diesel")                           |
| `body`       | string | Body type (e.g., "cargo-van")                        |
| `drivetrain` | string | Drivetrain (e.g., "all-wheel-drive")                 |

#### 🧪 Sample Request (Postman)

```json
{
  "make": "Mercedes-Benz",
  "model": "Sprinter 2500",
  "year": 2023,
  "engine": "16V DDI DOHC Turbo Diesel",
  "cylinders": 4,
  "fuel": "diesel",
  "body": "cargo-van",
  "drivetrain": "all-wheel-drive"
}
```

#### 📅 Sample Response

```json
{
  "predicted_price": 71913.65
}
```

---

## 🔄 Folder Structure

```
CAR-PRICE-PREDICTION/
├── web/
│   ├── backend/
│   │   ├── app/
│   │   │   ├── main.py           # FastAPI main app
│   │   │   ├── model.py          # ML model loading and prediction logic
│   │   │   ├── schemas.py        # Pydantic schemas for validation
│   │   ├── artifacts/            # Contains preprocessing pipelines and trained models
│   │   ├── requirements.txt      # Required packages
│   │   └── test_pipeline.py      # Testing and evaluation
```

---

## 🌍 CORS Setup (Cross-Origin)

CORS has been configured to allow requests from all origins:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## ✅ To Do

* Add Swagger UI customization
* Improve data validation
* Add CI/CD with GitHub Actions

---

## 🙌 Acknowledgements

Special thanks to the open-source community and the Render platform for free hosting!
