from fastapi import APIRouter
from ml_engine.predict import predict_climate_risk
from ml_engine.risk_engine import risk_reasoning
from genai_engine.reasoning import generate_ai_report

router = APIRouter()

@router.get("/predict")
def predict(year:int, month:int, t12:float, t24:float, anomaly:float):

    result = predict_climate_risk(year, month, t12, t24, anomaly)
    risk = risk_reasoning(result["class"], result)

    return {
        "prediction": result,
        "risk": risk
    }


@router.post("/analyze")
def analyze(payload:dict):

    report = generate_ai_report(payload)
    return {"report": report}
