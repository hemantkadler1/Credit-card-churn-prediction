from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI(title="Churn Prediction API")

with open("churn_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.post("/predict")
def predict_churn(features: dict):
    """
    Expects numerical feature values as input
    Returns churn prediction
    """
    try:
        input_data = np.array(list(features.values())).reshape(1, -1)

        prediction = model.predict(input_data)[0]

        return {
            "churn_prediction": int(prediction),
            "message": "Attrited Customer" if prediction == 1 else "Existing Customer"
        }

    except Exception as e:
        return {
            "error": str(e)
        }
