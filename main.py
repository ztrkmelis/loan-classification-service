from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from app import routes


app = FastAPI()


class ResponseIn(BaseModel):
    loanId: Optional[str] = None


class ResponseOut(BaseModel):
    response: dict


@app.get("/")
async def index():
    return "koc-finans-loan-prediction-service"


@app.post("/koc-finans-loan-prediction-service", response_model=ResponseOut)
async def get_client_segment(request: ResponseIn):
    loan_id = request.loanId
    result_dict = routes.get_prediction(loan_id)

    return {"response": result_dict}


